# Assignment
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
class Book(Base):
    __tablename__ = 'ook'
    id = Column(Integer, primary_key = True)
    title = Column(String, nullable = False)
    author = Column(String, nullable = False)
    price = Column(Float, nullable = False)

engine = create_engine('sqlite:///store1.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
new_book = Book(title = "Gastby",author= "Reshna and Samikxya", price = 299.99)
session.add(new_book)
session.commit()
# Query book
for book in session.query(Book):
    print(book.title, book.author, book.price)