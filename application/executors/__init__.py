from abc import ABC, abstractmethod


class ExecutorObserver(ABC):
    @abstractmethod
    def update(self, payment):
        """
        Abstract method for observers to update their state.
        """

