from typing import List

from application.executors.logger import PaymentLogger
from application.executors.writter import PaymentWriter
from application.file_reader import PaymentFileReader
from domain.payment import Payment
from domain.payment_methods.cash import CashPayment
from domain.payment_methods.credit import CreditPayment
from domain.payment_methods.debit import DebitPayment
from domain.payment_methods.pse import PsePayment
from application.payment_processor import PaymentProcessor


def main():
    processor = create_processor()
    payments = read_file("payment_details.json")
    start_process(processor, payments)


def create_processor() -> PaymentProcessor:
    processor = PaymentProcessor()

    # Payment methods
    cash = CashPayment()
    cash.add_observer(PaymentLogger)
    cash.add_observer(PaymentWriter)

    credit = CreditPayment()
    credit.add_observer(PaymentLogger)
    credit.add_observer(PaymentWriter)


    debit = DebitPayment()
    debit.add_observer(PaymentLogger)
    debit.add_observer(PaymentWriter)

    pse = PsePayment()
    pse.add_observer(PaymentLogger)
    pse.add_observer(PaymentWriter)

    processor.add_payment_method("cash", cash)
    processor.add_payment_method("credit", credit)
    processor.add_payment_method("debit", debit)
    processor.add_payment_method("pse", pse)

    return processor


def read_file(file_path: str) -> List[Payment]:
    file_reader = PaymentFileReader(file_path)
    payments_data = file_reader.read_payments_from_file()
    return [Payment(**payment_data) for payment_data in payments_data]


def start_process(processor: PaymentProcessor, payments: List[Payment]) -> None:
    for payment in payments:
        processor.process_payment(payment)


if __name__ == "__main__":
    main()
