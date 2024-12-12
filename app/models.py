from sqlalchemy import Column, Date, Integer, String, Boolean
from database import Base

# Define Model
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    due_date = Column(Date, nullable=True)


class User(Base):
    __tablename__ = "Lee_bo_xun"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True)
    password = Column(String, nullable=True)
    email = Column(String, nullable=True)