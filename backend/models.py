from sqlalchemy import Column, Integer, String
from database import Base

class Lead(Base):
    __tablename__="leads"
    
    id=Column(Integer, primary_key=True, index=True)
    
    name=Column(String)
    email=Column(String)
    phone=Column(String)
    source=Column(String)
    message=Column(String)
    classification=Column(String)
    suggested_reply=Column(String)
    status=Column(String, default="new")
    
    