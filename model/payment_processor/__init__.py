from abc import ABC, abstractmethod


class AbstractPaymentProcessor(ABC):
    @abstractmethod
    def add_payment_method(self, payment_method, strategy):
        pass

    @abstractmethod
    def remove_payment_method(self, payment_method):
        pass

    @abstractmethod
    def process_payment(self, payment_method, amount):
        pass


class PaymentProcessor(AbstractPaymentProcessor):
    def __init__(self):
        self.payment_strategies = {}

    def add_payment_method(self, payment_method, strategy):
        """Add a payment method to the processor"""
        self.payment_strategies[payment_method] = strategy

    def remove_payment_method(self, payment_method):
        """Remove a payment method from the processor"""
        if payment_method in self.payment_strategies:
            del self.payment_strategies[payment_method]

    def process_payment(self, payment_method, amount):
        """Process a payment using the specified payment method"""
        if payment_method in self.payment_strategies:
            strategy = self.payment_strategies[payment_method]
            strategy.process_payment(amount)
        else:
            print(f"Error: Payment method '{payment_method}' not found.")
