from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Welcome to the Personal Finance Tracker API!"}

@app.post("/transactions", response_model=schemas.TransactionResponse)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    new_transaction = models.Transaction(**transaction.model_dump())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

@app.get("/transactions", response_model=list[schemas.TransactionResponse])
def read_transactions(db: Session = Depends(get_db)):
    return db.query(models.Transaction).all()

@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    db.delete(transaction)
    db.commit()
    return {"message": "Transaction deleted successfully"}

@app.put("/transactions/{transaction_id}", response_model=schemas.TransactionResponse)
def update_transaction(transaction_id: int, updated_transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    existing_transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

    if existing_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    existing_transaction.description = updated_transaction.description
    existing_transaction.amount = updated_transaction.amount
    existing_transaction.category = updated_transaction.category
    existing_transaction.type = updated_transaction.type

    db.commit()
    db.refresh(existing_transaction)
    return existing_transaction
    