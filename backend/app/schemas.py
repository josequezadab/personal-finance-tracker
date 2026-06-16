from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    description: str
    amount: float
    category: str
    type: str

class TransactionResponse(BaseModel):
    id: int
    description: str
    amount: float
    date: datetime
    category: str
    type: str

    class Config:
        from_attributes = True