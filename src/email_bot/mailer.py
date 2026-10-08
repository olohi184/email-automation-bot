"""Secure SMTP email delivery with a dry-run option."""
import smtplib
import ssl
from email.message import EmailMessage


def build_message(sender: str, recipient: str, subject: str, body: str) -> EmailMessage:
    if not all(value.strip() for value in (sender, recipient, subject, body)):
        raise ValueError("Sender, recipient, subject and body are required")
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)
    return message


def send_message(message: EmailMessage, host: str, port: int, username: str, password: str) -> None:
    if not all((host, username, password)):
        raise ValueError("SMTP host and credentials are required")
    if not 1 <= port <= 65535:
        raise ValueError("SMTP port must be between 1 and 65535")
    context = ssl.create_default_context()
    if port == 465:
        with smtplib.SMTP_SSL(host, port, timeout=15, context=context) as server:
            server.login(username, password)
            server.send_message(message)
    else:
        with smtplib.SMTP(host, port, timeout=15) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(username, password)
            server.send_message(message)
