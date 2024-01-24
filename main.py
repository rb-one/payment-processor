from collections.abc import Mapping
from model.payment_methods.cash import CashPayment
from model.payment_methods.credit import CreditPayment
from model.payment_methods.debit import DebitPayment
from model.payment_methods.pse import PsePayment
from model.payment_processor import PaymentProcessor
from model.file_reader import PaymentFileReader


def main():
    processor = create_processor()
    payments = read_file("payments.json")
    start_process(processor, payments)


def create_processor() -> PaymentProcessor:
    payment_processor = PaymentProcessor()
    payment_processor.add_payment_method("cash", CashPayment())
    payment_processor.add_payment_method("credit", CreditPayment())
    payment_processor.add_payment_method("debit", DebitPayment())
    payment_processor.add_payment_method("pse", PsePayment())
    return payment_processor


def read_file(file_path: str) -> Mapping:
    file_reader = PaymentFileReader(file_path)
    return file_reader.read_payments_from_file()


def start_process(processor: PaymentProcessor, payments: Mapping) -> None:
    for payment in payments:
        processor.process_payment(**payment)


if __name__ == "__main__":
    main()
