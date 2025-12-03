from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse

from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import List

from ..models import Bank, InterestRate
from ..database import engine
from ..config import templates

router = APIRouter(
    prefix="/banks",
    tags=["view"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_class=HTMLResponse)
async def get_banks(request: Request):
    with Session(engine) as session:
        banks = session.exec(select(Bank).limit(100)).all()
    
    return templates.TemplateResponse(
        name="banks.html",
        request=request,
        context={"banks": banks}
    )
