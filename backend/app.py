from fastapi import FastAPI, Depends, HTTPException
from database import engine
from models import Base
from schemas import ClassifyRequest
from llm import classify_lead
from sqlalchemy.orm import Session

from database import get_db
from models import Lead
from schemas import LeadCreate, LeadResponse

from typing import List
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app=FastAPI()

@app.get("/")
def home():
    return {"message": "The backend is running"}


@app.post("/classify")
def classify(request: ClassifyRequest):
    result=classify_lead(request.message)
    return result

@app.post("/lead")
def create_lead(
    lead: LeadCreate,
    db: Session=Depends(get_db)
):
    
    result=classify_lead(lead.message)
    
    new_lead=Lead(
        name=lead.name,
        email=lead.email,
        phone=lead.phone,
        source=lead.source,
        message=lead.message,
        classification=result["classification"],
        suggested_reply=result["suggested_reply"],
        status="new"
    )
    
    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)
    
    return {
        "message":"Lead Saved",
        "id":new_lead.id
    }
    
@app.get("/leads", response_model=List[LeadResponse])
def get_leads(db: Session=Depends(get_db)):
    leads=db.query(Lead).all()
    return leads

@app.patch("/lead/{lead_id}")
def mark_contacted(lead_id:int, db: Session=Depends(get_db)):
    lead=db.query(Lead).filter(Lead.id==lead_id).first()
    
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    
    lead.status="contacted"
    db.commit()
    
    return {"message":"Lead updated"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

