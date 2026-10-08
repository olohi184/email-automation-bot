"""Send or preview a reminder email."""
import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from email_bot.mailer import build_message, send_message


def main() -> int:
    parser = argparse.ArgumentParser(description="Preview or send an email reminder")
    parser.add_argument("--to", required=True, help="Recipient email address")
    parser.add_argument("--subject", required=True)
    parser.add_argument("--message", required=True, help="Plain-text reminder")
    parser.add_argument("--send", action="store_true", help="Actually send the email; default is preview")
    args = parser.parse_args()
    sender = os.getenv("SMTP_SENDER", "")
    if not sender and not args.send:
        sender = "preview@example.com"
    try:
        message = build_message(sender, args.to, args.subject, args.message)
        if not args.send:
            print("DRY RUN: no email sent.\n")
            print(message)
            return 0
        host = os.getenv("SMTP_HOST", "")
        port = int(os.getenv("SMTP_PORT", "587"))
        send_message(message, host, port, os.getenv("SMTP_USERNAME", ""), os.getenv("SMTP_PASSWORD", ""))
    except (ValueError, OSError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print("Email submitted to SMTP server.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
