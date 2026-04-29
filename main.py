from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal
from models import ContactModel
from database import engine
from models import Base

Base.metadata.create_all(bind=engine)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Contact(BaseModel):
    email: str
    message: str


@app.post("/contact")
def send_message(data: Contact):
    db = SessionLocal()
    new_data = ContactModel(email=data.email, message=data.message)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {"message": "Saved"}


@app.get("/messages")
def get_messages():
    db = SessionLocal()
    return db.query(ContactModel).all()
