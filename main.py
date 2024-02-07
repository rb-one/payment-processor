from collections.abc import Mapping
from model.payment_methods.cash import CashPayment
from model.payment_methods.credit import CreditPayment
from model.payment_methods.debit import DebitPayment
from model.payment_methods.pse import PsePayment
from model.payment_processor import PaymentProcessor
from model.file_reader import PaymentFileReader
from model.executors.logger import PaymentLogger


def main():
    processor = create_processor()
    payments = read_file("payments.json")
    start_process(processor, payments)


def create_processor() -> PaymentProcessor:
    processor = PaymentProcessor()

    # Payment methods
    cash = CashPayment().add_observer(PaymentLogger)
    credit = CreditPayment().add_observer(PaymentLogger)
    debit = DebitPayment().add_observer(PaymentLogger)
    pse = PsePayment().add_observer(PaymentLogger)

    processor.add_payment_method("cash", cash)
    processor.add_payment_method("credit", credit)
    processor.add_payment_method("debit", debit)
    processor.add_payment_method("pse", pse)

    return processor


def read_file(file_path: str) -> Mapping:
    file_reader = PaymentFileReader(file_path)
    return file_reader.read_payments_from_file()


def start_process(processor: PaymentProcessor, payments: Mapping) -> None:
    for payment in payments:
        processor.process_payment(payment)


if __name__ == "__main__":
    main()
