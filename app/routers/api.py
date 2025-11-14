from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import List
from ..models import Bank, InterestRate
# from ..dependencies import get_token_header


router = APIRouter()

router = APIRouter(
    prefix="/banks",
    tags=["api","banks"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/banks/", response_model=List[Bank], tags=["banks"])
def read_banks():
    with Session(engine) as session:
        banks = session.exec(select(Bank)).all()
        return banks
