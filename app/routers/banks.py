from datetime import datetime
from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse

from typing import List

from ..models import Bank, BankProduct
from .api import get_bank_products, get_product_types
from ..config import templates

router = APIRouter(
    prefix="/banks",
    tags=["view"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{product_type}", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
async def view_bank_products(request: Request, 
                             product_type: str = "HIGH_YIELD_SAVINGS"):
    product_types = get_product_types()["product_types"]
    data = {
    "page_title": "Top Rates | Top Bank Interest Rates Tracker",
    "site_name": "Top Rates",
    "nav_items": [{"label": pt["value"], "url": "/banks/" + pt["name"].lower().replace(" ", "-")} 
                  for pt in product_types],
    "category_title": "Top " + " ".join(product_type.split("_")).title() + " Rates",
    "last_updated": datetime.now().strftime("%B %d, %Y"),
    }
    products = get_bank_products(product_type=product_type.upper())  # Fetch products of the specified type
    return templates.TemplateResponse(
        name="index.html",
        request=request,
        context={"products": products, 
                 **data}
    )
