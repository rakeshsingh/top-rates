from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import List
from ..models import Bank, InterestRate
from ..database import engine

router = APIRouter()

router = APIRouter(
    prefix="/api/v1",
    tags=["api", "banks"],
    responses={404: {"description": "Not found"}},
)

@router.get("/banks/", response_model=List[Bank], tags=["banks"])
def get_banks():
    with Session(engine) as session:
        banks = session.exec(select(Bank).limit(100)).all()
        return banks

@router.get("/banks/{bank_id}", response_model=Bank, tags=["banks"])
def get_bank(bank_id: str):
    with Session(engine) as session:
        bank = session.get(Bank, bank_id)
        if not bank:
            raise HTTPException(status_code=404, detail="Bank not found")
        return bank
    
@router.get("/interest-rates/", response_model=List[InterestRate], tags=["interest rates"])
def get_interest_rates():
    with Session(engine) as session:
        rates = session.exec(select(InterestRate).limit(100)).all()
        return rates