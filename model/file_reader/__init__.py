import json


class PaymentFileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_payments_from_file(self):
        """read payments from a json file (like ACH files)"""
        with open(self.file_path, "r") as file:
            return json.load(file)
