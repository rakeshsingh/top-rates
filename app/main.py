import uvicorn

from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import List, Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

from .models import Bank, BankProduct
from .routers import api, banks
from .database import engine
from .config import templates

# FastAPI application
app = FastAPI(title="Bank Interest Rates Tracker")
app.include_router(api.router)
app.include_router(banks.router)

@app.get("/", response_class=HTMLResponse)
def get_root(request: Request):
    with Session(engine) as session:
        banks = session.exec(select(Bank).limit(10)).all()
    return templates.TemplateResponse("index.html", {"request": request, "banks": banks})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)