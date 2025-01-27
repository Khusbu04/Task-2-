import pandas as pd
import smtplib
from datatime import datatime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email="khusbumayasingh59@gmail.com"
receiver_email=""
password="mgev niev duex xnqe"

def load_data_from_file(file_path):
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print("\nFile path not found")