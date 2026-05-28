"""
Email Auto-Responder Service
"""

import smtplib
from email.mime.text import MIMEText
import imaplib
import email

CONFIG = {
    'smtp': 'smtp.mail.yahoo.com',
    'imap': 'imap.mail.yahoo.com',
    'email': 'davidmartin10127@yahoo.com',
    'app_password': 'figcdclugmsjsamr'
}

RESPONSE_RULES = {
    'inquiry': "Thank you for your interest! We'll get back to you within 24 hours.",
    'support': "We're here to help.",
    'meeting': "Thanks for reaching out about a meeting.",
}

def check_and_respond():
    mail = imaplib.IMAP4_SSL(CONFIG['imap'])
    mail.login(CONFIG['email'], CONFIG['app_password'])
    mail.select('INBOX')
    status, messages = mail.search(None, 'UNSEEN')
    email_ids = messages[0].split()
    
    responded = 0
    for eid in email_ids[-10:]:
        _, msg_data = mail.fetch(eid, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])
        subject = msg['subject'].lower()
        from_addr = msg['from']
        
        for keyword, response in RESPONSE_RULES.items():
            if keyword in subject:
                send_email(from_addr, f"Re: {msg['subject']}", response)
                responded += 1
                break
    mail.logout()
    return responded

def send_email(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = CONFIG['email']
    msg['To'] = to
    with smtplib.SMTP_SSL(CONFIG['smtp'], 465) as smtp:
        smtp.login(CONFIG['email'], CONFIG['app_password'])
        smtp.sendmail(CONFIG['email'], to, msg.as_string())

if __name__ == '__main__':
    print(f"Auto-responded to {check_and_respond()} emails")
