from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import List
from ..models import Bank, BankProduct, ProductType
from ..database import engine

router = APIRouter()

router = APIRouter(
    prefix="/api/v1",
    tags=["api", "banks", "bank products", "interest rates"],
    responses={404: {"description": "Not found"}},
)

@router.get("/product-types/", tags=["api", "bank products", "product types"])
def get_product_types():
    product_types = [{"name": pt.name, "value": pt.value} for pt in ProductType]
    return {"product_types": product_types}


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
    

@router.get("/bank-products/", response_model=List[BankProduct],  tags=["bank products", "interest rates"])
def get_bank_products(product_type:str = None):
    with Session(engine) as session:
        print(f"Fetching products for type: {product_type}")
        if product_type:
            product = session.exec(
                select(BankProduct).where(BankProduct.type == product_type).limit(100)
            ).all()
        else:
            product = session.exec(select(BankProduct).limit(100)).all()
        return product