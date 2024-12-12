from loguru import logger

from app.integrations.bill_pdf_generator.bill_pdf_generator import BillPDFGenerator
from app.integrations.email_sender.email_sender_abc import EmailSender
from app.models.bill import Bill
from app.repositories.bill_repository import BillRepository


class BillService:

    def __init__(
            self,
            bill_repo: BillRepository,
            email_sender: EmailSender,
            bill_generator: BillPDFGenerator,
    ):
        self.email_sender = email_sender
        self.bill_generator = bill_generator
        self.bill_repo = bill_repo


    def process_bill(self, bill: Bill):
        bill_in_database = self.bill_repo.find_one(filters={
            "debt_id": bill.debt_id
        })

        if bill_in_database is not None:
            bill = bill_in_database

        if bill.processed:
            return

        try:
            bill_pdf = self.bill_generator.generate_bill(
                government_id=bill.government_id,
                debt_amount=bill.debt_amount,
                debt_due_date=bill.debt_due_date
            )
            self.email_sender.send_email(
                _from="kanastra@kanastra.com",
                to=bill.email,
                body="Voce recebeu um boleto para pagar!",
                file=bill_pdf
            )

            bill.processed = True
        except Exception as ex:
            logger.error(f"Error in __process_line - Error {ex}")
            bill.processed = False
        finally:
            self.bill_repo.save(bill)
