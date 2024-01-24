import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


class PaymentLogger:
    def log_payment_info(self, payment_method, amount):
        """Register payment info"""
        logger.info(f"Payment processed - Method: {payment_method}, Amount: ${amount}")
