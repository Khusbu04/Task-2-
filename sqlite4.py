# Assignment wrong
import request 
import csv
import smtplib
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def file_csv_for_totals(fake_store):
    row_totals = {}
    colummn_totals = {}
    with open(file_path, mode = "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
Base = declarative_base()
class Elements(Base):
    __tablename__ = 'elements'
    product = Column(Integer, primary_key = True)
    quantity = Column(Float, nullable = False)
    price = Column(Float, nullable = False)
    customer_email = Column(String, nullable = False)
def fetch_product_details(fake_store):
    base_url = "https://fakestoreapi.com/"
response = request.get(url)
if response.status_code == 200:
    print("Code fetched successfully!\n")
    code_data
sender_email = "khusbumayasingh59@gmail.com"
receiver_email = "rumancha12@gmail.com"
password = "mgev niev duex xnqe"
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")


