# NSP PHP Bootcamp Email Sender

This is a simple Flask application that sends HTML emails to a list of recipients. It allows users to input email addresses separated by commas, and it sends an email to each recipient individually using the configured mail server.

## Features

- Sends HTML emails using Flask-Mail.
- Configurable mail settings for SMTP.
- Accepts multiple recipient email addresses via a form input.
- Utilizes a custom email template for the email body.

## Prerequisites

Before running the app, make sure you have the following installed:

- Python (3.x recommended)
- Flask
- Flask-Mail

To install the required Python libraries, you can use pip:

```bash
pip install Flask Flask-Mail
```

```python
MAIL_SERVER: The SMTP server (e.g., smtp.hostinger.com).
MAIL_PORT: The SMTP port (usually 465 for SSL or 587 for TLS).
MAIL_USE_SSL: Set to True for SSL.
MAIL_USERNAME: Your email address (e.g., info@nspspace.com).
MAIL_PASSWORD: The password for your email account.
MAIL_DEFAULT_SENDER: The default sender email (e.g., info@nspspace.com).
