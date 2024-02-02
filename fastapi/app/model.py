# models.py
from sqlalchemy import Column, Integer, String, Boolean
from config import Base

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)