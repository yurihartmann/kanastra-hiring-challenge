from tempfile import TemporaryFile
from loguru import logger

from app.integrations.email_sender.email_sender_abc import EmailSender


class SmtpEmailSender(EmailSender):

    def __init__(self):
        logger.info("Configuring SmtpEmailSender")

    def send_email(self, _from: str, to: str, body: str, file: TemporaryFile):
        logger.info(f"Sending email {_from=} {to=}...")