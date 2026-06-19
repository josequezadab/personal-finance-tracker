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
    category: str
    type: str
    date: datetime

    class Config:
        from_attributes = True