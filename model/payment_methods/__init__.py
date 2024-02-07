from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, payment):
        """
        Abstract method to process a payment.
        It must be implemented by the child classes.
        """


class ObservablePaymentMethod(PaymentMethod):
    """
    Payment method that allows to add a list of observers
    to execute actions
    """

    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
        return self

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, amount):
        for observer in self._observers:
            observer.update(type(self).__name__, amount)
