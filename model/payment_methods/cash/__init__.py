from model.payment_methods import ObservablePaymentMethod

# from model.logger import PaymentLogger


class CashPayment(ObservablePaymentMethod):
    def process_payment(self, payment):
        """implementes abstract method"""
        self.notify_observers(payment.apply_charge())
