from model.payment_methods import ObservablePaymentMethod


class DebitPayment(ObservablePaymentMethod):
    def process_payment(self, payment):
        """implementes abstract method"""
        self.notify_observers(payment)
