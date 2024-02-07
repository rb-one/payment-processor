from abc import ABC, abstractmethod


class ExecutorObserver(ABC):
    @abstractmethod
    def update(self, messege):
        """
        Abstract method for observers to update their state.
        """
