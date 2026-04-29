# models.py
from sqlalchemy import Column, Integer, String
from database import Base


class ContactModel(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    message = Column(String)
