from datetime import datetime
from loguru import logger

class BillPDFGenerator:

    def generate_bill(self, government_id: int, debt_amount: float, debt_due_date: datetime) -> str:
        bill = f"Bill({government_id=} {debt_amount=} {debt_due_date=})"
        logger.info(f"Generated {bill}")
        return bill
