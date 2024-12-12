from sqlmodel import Session

from app.constants import EngineType
from app.models.bill import Bill
from sqlmodel import select


class BillRepository:

    def __init__(self, engine: EngineType):
        self.engine = engine

    def find_one(self, filters: dict[str, any] = None) -> Bill | None:
        with Session(self.engine) as s:
            filters = filters if filters else {}
            query = select(Bill).filter_by(**filters)
            return s.scalar(query)

    def save(self, bill: Bill):
        with Session(self.engine) as s:
            s.add(bill)
            s.commit()
