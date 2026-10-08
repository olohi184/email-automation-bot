"""Unit tests; no actual emails are sent."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from email_bot.mailer import build_message, send_message


class MailerTests(unittest.TestCase):
    def test_message(self):
        msg = build_message("from@example.com", "to@example.com", "Reminder", "Hello")
        self.assertEqual(msg["Subject"], "Reminder")
        self.assertEqual(msg.get_content().strip(), "Hello")

    def test_missing_body(self):
        with self.assertRaises(ValueError):
            build_message("from@example.com", "to@example.com", "Reminder", "")

    @patch("email_bot.mailer.smtplib.SMTP")
    def test_starttls(self, smtp):
        msg = build_message("from@example.com", "to@example.com", "Reminder", "Hello")
        send_message(msg, "smtp.example.com", 587, "username", "password")
        server = smtp.return_value.__enter__.return_value
        server.starttls.assert_called_once()
        server.login.assert_called_once_with("username", "password")
        server.send_message.assert_called_once_with(msg)


if __name__ == "__main__":
    unittest.main()
