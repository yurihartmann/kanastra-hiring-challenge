from datetime import datetime
from time import sleep

from app.constants import QueueReader
from app.models.bill import Bill
from app.services.v1.bill.bill_service import BillService


class FileProcessorTask:

    def __init__(
            self,
            bill_service: BillService,
            queue: QueueReader
    ):
        self.bill_service = bill_service
        self.queue = queue

    def __message_to_bill(self, line: str) -> Bill:
        try:
            data = line.split(",")
            return Bill(
                    name=data[0],
                    government_id=int(data[1]),
                    email=data[2],
                    debt_amount=float(data[3]),
                    debt_due_date=datetime.strptime(data[4], "%Y-%m-%d"),
                    debt_id=data[5],
                    processed=False,
            )

        except Exception as e:
            print(f"Error in __read_line - Error: {e}")
            raise Exception()

    def start_consume_lines(self):
        print("Started task to consume lines")
        while True:
            message = self.queue.get()
            if not message:
                sleep(1)
                continue

            bill = self.__message_to_bill(message)
            self.bill_service.process_bill(bill)
