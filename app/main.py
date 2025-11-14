import os
import uvicorn

from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import List, Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

from .models import Bank, InterestRate
from .routers import api, banks

# Database configuration
DATABASE_NAME = "top_rates.db"
sqlite_url = f"sqlite:///{DATABASE_NAME}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session

# FastAPI application
app = FastAPI(title="Bank Interest Rates Tracker")
# Get the directory of the current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Set the directory for templates
template_dir = os.path.join(BASE_DIR, 'templates')
templates = Jinja2Templates(directory=template_dir)

@app.get("/", response_class=HTMLResponse)
async def get_banks(request: Request):
    with Session(engine) as session:
        banks = session.exec(select(Bank).limit(100)).all()
    
    return templates.TemplateResponse(
        name="banks.html",
        request=request,
        context={"banks": banks}
    )


@app.get("/banks", response_model=List[Bank])
def read_banks():
    with Session(engine) as session:
        banks = session.exec(select(Bank).limit(100)).all()
        return banks


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)