import os

from loguru import logger
from dishka import Provider, Scope, provide

from app.constants import EngineType, QueueReader, QueueWriter
from app.integrations.bill_pdf_generator.bill_pdf_generator import BillPDFGenerator
from app.integrations.email_sender.email_sender_abc import EmailSender
from app.integrations.email_sender.smtp_email_sender import SmtpEmailSender
from app.queue.RabbitMQQueue import RabbitMQQueue
from app.repositories.bill_repository import BillRepository
from app.services.v1.bill.bill_service import BillService
from app.services.v1.file_processor.file_processor_service import FileProcessorService
from sqlmodel import create_engine

from app.tasks.file_processor_task import FileProcessorTask



class ServicesProvider(Provider):
    scope = Scope.REQUEST

    # Database
    @provide(scope=Scope.APP)
    def engine(self) -> EngineType:
        return create_engine(os.getenv("DATABASE_URL"))

    @provide(scope=Scope.APP)
    def queue_reader(self) -> QueueReader:
        queue_name = "bill_to_process"
        r = RabbitMQQueue(
            queue_name=queue_name,
            host=os.getenv("HOST_RABBITMQ")
        )
        r.channel.queue_declare(queue_name)
        logger.info(f"Channel criado: {queue_name=}")
        return r

    @provide(scope=Scope.APP)
    def queue_writer(self) -> QueueWriter:
        queue_name = "bill_to_process"
        r = RabbitMQQueue(
            queue_name=queue_name,
            host=os.getenv("HOST_RABBITMQ")
        )
        return r

    bill_repo = provide(BillRepository, scope=Scope.APP)

    # Integrations
    bill_pdf_generator = provide(BillPDFGenerator, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def email(self) -> EmailSender:
        return SmtpEmailSender()

    # Service
    fps = provide(FileProcessorService)
    fpt = provide(FileProcessorTask, scope=Scope.APP)
    bs = provide(BillService)
    bs_singleton = provide(BillService, scope=Scope.APP)

