import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

from model.executors import ExecutorObserver


class PaymentLogger(ExecutorObserver):
    def update(self, payment):
        """Register payment info"""
        logger.info(payment.__dict__)
