import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_SENDER, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT

async def send_appeal_email(phone_number: str, reason: str = "Login issue / Account restricted"):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = "support@whatsapp.com"
    msg['Subject'] = f"Appeal for Account: {phone_number}"

    body = f"""
    Dear WhatsApp Support,
    
    I am experiencing issue with my account:
    Phone: {phone_number}
    Problem: {reason}
    
    Please review and restore my account.
    Thank you.
    """
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False
