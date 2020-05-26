import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

from src.settings import settings


def send_error_email(email_from_address, email_from_pwd, email_to_address, error):
    """
        Sends an email with error message.

        Parameters
        ----------
        email_from_address: str
            Email address of sender of error email.
        email_from_pwd: str
            Password to email of sender of error email.
        email_to_address: str
            Email address of recipient of error email.
        error: str
            Error to be sent.
    """

    message = MIMEMultipart('alternative')
    message['Subject'] = 'Error of GS Automation'
    message['From'] = email_from_address
    message['To'] = email_to_address

    message.attach(MIMEText(f'''
        <html>
          <body>
            <h5>Following error happened in GS Automation vm instance in GCP:</h5>
            <p>{error}</p>
          </body>
        </html>
    ''', 'html'))

    try:
        with smtplib.SMTP_SSL(settings.SMTP_SERVER, settings.SMTP_PORT, context=ssl.create_default_context()) as server:
            server.login(email_from_address, email_from_pwd)
            server.sendmail(email_from_address, email_to_address, message.as_string())
    except Exception as e:
        logging.getLogger(str(settings.PROJECT_DIR)).warning(f'Unable to send email with error, reason is: {e}')
