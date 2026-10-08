# Email Automation Bot — Python CLI

A secure starter project for **previewing and sending plain-text email reminders** using SMTP. Built as a reusable Python package with a command-line interface and mocked tests.

> **Project status:** This repository previously contained only a one-line README. The current implementation is a new starter application, not a refactor of existing code. It sends individual reminders on demand; recurring scheduling and automatic reminder queues are not yet implemented.

## Requirements
- Python 3.10+
- An SMTP account that permits authenticated email submission
- Provider-specific app password or SMTP credentials (never commit these)

## Preview (no credentials required)
```bash
python main.py --to recipient@example.com --subject "Meeting reminder" --message "Our meeting is tomorrow."
```

## Send an email
Set the variables in `.env.example` **in your terminal environment** using your actual SMTP provider's settings. The program does not automatically read a `.env` file.

macOS/Linux example:
```bash
export SMTP_HOST="smtp.example.com"
export SMTP_PORT="587"
export SMTP_SENDER="you@example.com"
export SMTP_USERNAME="your_username"
export SMTP_PASSWORD="your_app_password"
python main.py --to recipient@example.com --subject "Reminder" --message "Please review the report." --send
```

Windows PowerShell uses `$env:SMTP_HOST="..."` and the corresponding `$env:` variables. **Use a real provider host, not `smtp.example.com`.** Port 465 uses implicit TLS; other configured ports use STARTTLS.

## Test
```bash
python -m unittest discover -s tests -v
```

## Structure
- `main.py`: CLI with safe dry-run default
- `src/email_bot/mailer.py`: message creation and SMTP delivery
- `tests/`: mocked tests (no network connection required)
- `.env.example`: names of required configuration variables, not actual secrets

## Safety and limitations
Only send email to recipients who expect it. No mass mailing, recurring schedule, queue, or delivery tracking is implemented. Successful SMTP submission does not guarantee inbox delivery. Avoid passing confidential messages directly as command-line arguments on shared computers.

## Author
Olohimai Juliet Michael · [GitHub](https://github.com/olohi184)
