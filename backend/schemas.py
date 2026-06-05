from pydantic import BaseModel

class LeadCreate(BaseModel):
    name:str
    email:str
    phone:str
    source:str
    message:str
    
class ClassifyRequest(BaseModel):
    message:str
    
class LeadResponse(BaseModel):
    id:int
    name:str
    email:str
    phone:str
    source:str
    message:str
    classification:str
    suggested_reply:str
    status:str
    
    class Config:
        from_attributes=True