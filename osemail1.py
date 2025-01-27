 # Assignment Task 1: Write a Python script that sends an email with the contents of a CSV file (e.g., a sales report) as an attachment.
 import smtplib
 from email.mine.text import MIMEText
 from email.mine.multipart import MIMEMultipart
 from email.mine.base import MIMEBase
 from email import encoders
 # Email Credentials
 sender_email = "khusbumayasingh59@gmail.com"
 receiver_email = "rumancha12@gmail.com"
 password = "mgev niev duex xnque"
 def send_email_with_attachment(csv_path):
    """Send an email with the sprcified CSV file as an attachment."""
    try:
        # Email contents
        subject = "Sales Report"
        body = (
            "Hello, \n\n"
            "Please find the attached sales report.\n"
            "Let me know if you have any questions. \n\n"
            "Best regards, \nYour Automated Email Bot"
)
message = MIMEMultipart()
message["From"] = sender_email
message["TO"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))
if os.path.exists(csv_path):
    print("CSV fiel found. Attaching the file...")
    with open(csv_path, 'rb') as file:
        attachment = MIMEBase(('application', 'octet-stream')
        attachment.set_payload(file.read())
    encoders.encode_base64(attachment)
    attachmnet.add_header(
        
    )