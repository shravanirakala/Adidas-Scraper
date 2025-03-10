import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from rich.console import Console

console = Console()

def send_email(plain_text: str, html: str, recipient_email: str) -> str:
    """Sends an email notification."""
    
    
    email = MIMEMultipart("alternative")

    formatter_sender  = formataddr((os.getenv("SENDER_NAME"), os.getenv("SENDER_EMAIL")))
    email["From"] = formatter_sender
    email["To"] = recipient_email
    email["Subject"] = "Adidas Discount Notification"
    
    smtp_server = "smtp.mail.me.com"
    smtp_port = 587
    smtp_username = os.getenv("SENDER_EMAIL")
    smtp_password = os.getenv("ICLOUD_APP_PASSWORD")
    
    

    if not smtp_username or not smtp_password:
        console.print("[bold red]Email credentials not set in environment variables![/bold red]")
        return "Email not sent!"

    try:
        email.attach(MIMEText(plain_text, "plain"))
        email.attach(MIMEText(html, "html"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(email)
        
        return "Email sent successfully!"
    except Exception as e:
        console.print(f"[bold red]Error sending email: {e}[/bold red]")
        return "Email not sent!"
