from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database import get_engine, Session

Base = declarative_base()

# Define todo model
class ToDoItem(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String, nullable=False)
    complete = Column(Boolean, default=False)

# create db
def create_db():
    engine = get_engine()
    Base.metadata.create_all(engine)

# Add task
def add_task(task:str):
    session = Session()
    new_task = ToDoItem(task=task)
    session.add(new_task)
    session.commit()
    session.close()

# Function to get all tasks
def get_tasks():
    session = Session()
    tasks = session.query(ToDoItem).all()
    session.close()
    return tasks

# Modify task
def modify_task(task_id:int, new_task:str, complete:bool):
    session = Session()
    task = session.query(ToDoItem).filter(ToDoItem.id == task_id).first()
    if task:
        task.task = new_task
        task.complete = complete
        session.commit()
    session.close()

def delete_task(task_id:int):
    session = Session()
    task = session.query(ToDoItem).filter(ToDoItem.task == task_id)
    if task:
        session.delete(task)
        session.commit()
    session.close()
