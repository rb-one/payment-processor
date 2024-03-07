from domain.payment_methods import ObservablePaymentMethod


class PsePayment(ObservablePaymentMethod):
    def process_payment(self, payment):
        """implementes abstract method"""
        self.notify_observers(payment.apply_charge())
