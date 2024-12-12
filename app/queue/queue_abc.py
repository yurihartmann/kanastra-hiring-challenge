from abc import ABC, abstractmethod

class QueueABC(ABC):

    @abstractmethod
    def get(self) -> str:
        """Not Implemented"""

    @abstractmethod
    def put(self, data: str):
        """Not Implemented"""