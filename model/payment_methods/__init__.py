from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """
        Abstract method to process a payment.
        It must be implemented by the child classes.
        """
