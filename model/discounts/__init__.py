from abc import ABC, abstractmethod
from collections.abc import Mapping

class DiscountDecorator(ABC):
    @abstractmethod
    def __init__(self, payment, discount):
        pass

    @abstractmethod
    def apply(self) -> Mapping:
        pass


class PercentageDiscount(DiscountDecorator):
    def __init__(self, payment, discount):
        self.payment = payment
        self.discount = discount

    def apply(self) -> Mapping:
        discount_amount = self.payment["amount"] * (self.discount / 100)

        if to_charge := self.payment.get("to_charge"):
            to_charge -= discount_amount
        else:
            to_charge = self.payment["amount"] - discount_amount

        return {**self.payment, "to_charge": to_charge}


class TotalAmountDiscount(DiscountDecorator):

    def __init__(self, payment, discount):
        self.payment = payment
        self.discount = discount

    def apply(self) -> Mapping:

        if to_charge := self.payment.get("to_charge"):
            to_charge -= abs(self.discount)
        else:
            to_charge = self.payment["amount"] - abs(self.discount)

        return {**self.payment, "to_charge": to_charge}


class DiscountPaymentFactory:
    def create_discount(self, discount, payment):

        if discount.get("discount_type") == "total_amount":
            payment = TotalAmountDiscount(payment, discount["value"])
        elif discount.get("discount_type") == "percentage":
            payment = PercentageDiscount(payment, discount["value"])

        return payment

