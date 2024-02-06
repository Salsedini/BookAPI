# models.py
from sqlalchemy import Column, Integer, String
from config import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

