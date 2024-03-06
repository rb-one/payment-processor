from abc import ABC, abstractmethod
from collections.abc import Mapping


class DiscountDecorator(ABC):
    @abstractmethod
    def apply_charge(self) -> Mapping:
        pass


class PercentageDiscount(DiscountDecorator):
    def __init__(self, payment, discount):
        self.payment = payment
        self.discount = discount

    def apply_charge(self) -> Mapping:
        self.payment = self.payment.apply_charge()
        percentage = self.discount / 100

        if self.payment.to_charge:
            self.payment.to_charge -= self.payment.to_charge * percentage
        else:
            discount_amount = self.payment.amount * percentage
            self.payment.to_charge = self.payment.amount - discount_amount

        return self.payment


class TotalAmountDiscount(DiscountDecorator):
    def __init__(self, payment, discount):
        self.payment = payment
        self.discount = discount

    def apply_charge(self) -> Mapping:
        self.payment = self.payment.apply_charge()

        if self.payment.to_charge:
            self.payment.to_charge -= abs(self.discount)
        else:
            self.payment.to_charge = self.payment.amount - abs(self.discount)
        return self.payment


class DiscountPaymentFactory:
    def create_discount(self, discount, payment):
        if discount.get("discount_type") == "total_amount":
            payment = TotalAmountDiscount(payment, discount["value"])
        elif discount.get("discount_type") == "percentage":
            payment = PercentageDiscount(payment, discount["value"])

        return payment
