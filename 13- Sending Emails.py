from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "John Doe"
message["to"] = "testuser@testsite.com"
message["subject"] = "This is a test"

message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testuser@testsite.com", "writehereapassword")
    smtp.send_message(message)
    print("Email has been sent.")