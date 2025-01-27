# Using SQLite3 to interact with a database
import sqlite3 
connection = sqlite3.connect("store.db")
cursor = connection.cursor()
# Create a table for products
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
)''')
# Insert data
cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("Laptop", 999.99 ))
connection.commit()
# Fetch data
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)
connection.close()
# Using SQLAlchemy for database interaction
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    price = Column(Float, nullable = False)
# Create engine and session
engine = create_engine('sqlite:///store.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
# Add a new product
new_product = Product(name = "Tablet", price = 299.99)
session.add(new_product)
session.commit()
# Query products
for product in session.query(Product):
    print(product.name, product.price)