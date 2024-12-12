from abc import ABC, abstractmethod
from tempfile import TemporaryFile


class EmailSender(ABC):

    @abstractmethod
    def send_email(self, _from: str, to: str, body: str, file: TemporaryFile):
        """Not Implemented"""