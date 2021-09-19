from email import encoders
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

class Email:
    server = "smtp.gmail.com"
    port = 465

    def __init__(self, src_mail: str, friendly_name: str):
        self.src = src_mail
        self.sendName = friendly_name
        context = ssl.create_default_context()
        self.smtp_relay = smtplib.SMTP_SSL(self.server, self.port, context=context)
        self.smtp_relay.login(self.src, input(f"Enter password for {self.src}: "))
    
    def newMail(self, dest_mail: str, dest_name: str, subj: str, body: str):
        self.mail = MIMEMultipart()
        self.mail['From'] = f"{self.sendName}<{self.src}>"
        self.mail['To'] = f"{dest_name}<{dest_mail}>"
        self.dst = dest_mail
        self.mail['Subject'] = subj
        # self.mail.attach(MIMEText(body, "plain"))
        self.mail.attach(MIMEText(body, "html"))
        
    def attach(self, attachment_name: str, attachment_path: str):
        attachment = MIMEBase("application", "octet-stream")
        attachment.set_payload(open(attachment_path, 'rb').read())
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", f"attachment; filename= {attachment_name}")
        self.mail.attach(attachment)
    
    def send(self):
        self.smtp_relay.sendmail(self.src, self.dst, self.mail.as_string())
        print(f"Mail Sent to {self.dst}!!")