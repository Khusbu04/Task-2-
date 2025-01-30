#Assignment wrong
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date

Base=declarative_base()
engine=create_engine('sqlite:///todolistdb.db')
Session=sessionmaker(bind=engine)
session=Session()

class Task(Base):
    tablename = 'tasks'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    due_date = Column(Date, nullable=True)

Base.metadata.create_all(engine)

def add_task(description, due_date=None):
    new_task=Task(description=description, due_date=due_date)
    session.add(new_task)
    session.commit()
    print("Task added successfully")


def remove_task(task_id):
    task=session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        print(f"Task {task_id} removed.")
    else:
        print("Task not found...")

def view_tasks():
    tasks=session.query(Task).all()
    for task in tasks:
         print(f"ID: {task.id}, Description: {task.description}, Due Date: {task.due_date}")

add_task("Finish assignment", date(2025, 2, 1))
add_task("Go shopping", date(2025, 2, 1))
add_task("have night out", date(2025, 1, 3))
view_tasks()
remove_task(1)
view_tasks()

session.close()