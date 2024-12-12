import unittest
from unittest.mock import Mock

from app.services.v1.bill.bill_service import BillService
from tests.fixture.bill_factory import BillFactory


class BillServiceTest(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.bill_repo_mock = Mock()
        self.email_sender_mock = Mock()
        self.bill_generator_mock = Mock()
        self.bill_service = BillService(
            bill_repo=self.bill_repo_mock,
            email_sender=self.email_sender_mock,
            bill_generator=self.bill_generator_mock,
        )

    def test_process_bill(self):
        # Arrange
        self.bill_repo_mock.find_one.return_value = None
        self.bill_generator_mock.generate_bill.return_value = "..."
        bill = BillFactory.generate_bill()

        # Act
        self.bill_service.process_bill(
            bill=bill
        )

        # Assert
        self.bill_repo_mock.find_one.assert_called_once_with(filters={
            "debt_id": bill.debt_id
        })
        self.bill_repo_mock.save.assert_called_once()
        self.bill_generator_mock.generate_bill.assert_called_once()
        self.email_sender_mock.send_email.assert_called_once()
