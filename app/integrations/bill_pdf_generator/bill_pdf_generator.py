from datetime import datetime


class BillPDFGenerator:

    def generate_bill(self, government_id: int, debt_amount: float, debt_due_date: datetime) -> str:
        bill = f"Bill({government_id=} {debt_amount=} {debt_due_date=})"
        print(f"Generated {bill}")
        return bill
