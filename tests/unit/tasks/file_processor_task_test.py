import unittest
from datetime import datetime
from time import sleep
from unittest.mock import Mock

from loguru import logger

from app.constants import QueueReader
from app.exceptions.file_wrong_exception import FileWrongException
from app.models.bill import Bill
from app.services.v1.bill.bill_service import BillService
from app.tasks.file_processor_task import FileProcessorTask


class FileProcessorTaskTest(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.bill_service_mock = Mock()
        self.queue = Mock()
        self.fpt = FileProcessorTask(
            bill_service=self.bill_service_mock,
            queue=self.queue,
        )

    def test_message_to_bill_should_be_success(self):
        ## Arrange
        line = "Dennis Davis,7479,angela12@example.com,9269,2022-10-23,a65abc5f-4760-42a5-9dc3-a68526e48a5f"

        # Act
        bill = self.fpt._message_to_bill(line=line)

        # Assert
        self.assertIsInstance(bill, Bill)

    def test_message_to_bill_should_be_raise_error(self):
        ## Arrange
        line = "Dennis Davis48a5f"

        # Act and Assert
        with self.assertRaises(FileWrongException):
            self.fpt._message_to_bill(line=line)
