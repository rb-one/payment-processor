from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        """
        Abstract method to apply the discount.
        """


class PercentageDiscount(Discount):
    def apply_discount(self, payment):
        discount_amount = payment["amount"] * (payment["discount"] / 100)
        charge = payment["amount"] - discount_amount
        return {**payment, "to_charge": charge}


class TotalAmountDiscount(Discount):
    def apply_discount(self, payment):
        charge = payment["amount"] - abs(payment["discount"])
        return {**payment, "to_charge": charge}


class NoDiscount(Discount):
    def apply_discount(self, payment):
        return {**payment, "to_charge": payment["amount"]}


class DiscountPaymentFactory:
    def create_discount(self, payment):
        if payment.get("discount_type") == "total_amount":
            discount = TotalAmountDiscount()
        elif payment.get("discount_type") == "percentage":
            discount = PercentageDiscount()
        else:
            discount = NoDiscount()
        return discount


class DiscountedPaymentDecorator:
    def __init__(self, payment_strategy):
        self._payment_strategy = payment_strategy

    def process_payment(self, payment):
        self._discount = DiscountPaymentFactory().create_discount(payment)
        updated_payment = self._discount.apply_discount(payment)
        self._payment_strategy.process_payment(updated_payment)
