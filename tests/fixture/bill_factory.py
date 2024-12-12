import random
import uuid
from datetime import datetime

from app.models.bill import Bill


class BillFactory:

    @classmethod
    def generate_bill(cls) -> Bill:
        return Bill(
            government_id=random.randint(1000, 9999),
            name="test",
            email="test@test.com",
            debt_amount=1000,
            debt_due_date=datetime.now(),
            debt_id=str(uuid.uuid4()),
            processed=False,
        )