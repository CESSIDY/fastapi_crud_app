from enum import Enum
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
