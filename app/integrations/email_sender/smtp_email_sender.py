from tempfile import TemporaryFile

from app.integrations.email_sender.email_sender_abc import EmailSender


class SmtpEmailSender(EmailSender):

    def __init__(self):
        print("Configuring SmtpEmailSender")

    def send_email(self, _from: str, to: str, body: str, file: TemporaryFile):
        print(f"Sending email {_from=} {to=}...")