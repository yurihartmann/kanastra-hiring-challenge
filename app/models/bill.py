from sqlmodel import SQLModel, Field
from sqlalchemy.types import BIGINT, VARCHAR
from datetime import datetime


class Bill(SQLModel, table=True):
    __tablename__ = "bills"

    government_id: int = Field(sa_type=BIGINT)
    name: str
    email: str
    debt_amount: float
    debt_due_date: datetime
    debt_id: str  = Field(primary_key=True, sa_type=VARCHAR(length=36))
    processed: bool
