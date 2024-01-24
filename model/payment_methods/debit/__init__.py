from model.payment_methods import PaymentMethod
from model.logger import PaymentLogger


class DebitPayment(PaymentMethod):
    def process_payment(self, amount):
        """implementes abstract method"""
        logger = PaymentLogger()
        logger.log_payment_info(type(self).__name__, amount)
