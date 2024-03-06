from abc import ABC, abstractmethod
from collections.abc import Mapping
from typing import List, Optional


class BasePayment(ABC):
    @abstractmethod
    def apply_charge(self) -> object:
        pass


class Payment(BasePayment):
    def __init__(
        self,
        payment_method: str,
        amount: float,
        discounts: List = [],
        to_charge: Optional[float] = None,
    ):
        self.payment_method = payment_method
        self.amount = amount
        self.discounts = discounts
        self.to_charge = to_charge

    def apply_charge(self):
        if not self.to_charge:
            self.to_charge = self.amount

        return self
