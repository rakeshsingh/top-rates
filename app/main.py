from datetime import datetime
import uvicorn

from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from typing import List, Optional
# from sqlmodel import Field, Session, SQLModel, create_engine, select

from .models import Bank, BankProduct, ProductType
from .routers import api, banks
# from .database import engine
# from .config import templates

# FastAPI application
app = FastAPI(title="Bank Interest Rates Tracker")
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)
app.include_router(banks.router)

@app.get("/")
async def redirect_old_path():
    return RedirectResponse(url="/banks")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)