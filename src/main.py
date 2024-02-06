from fastapi import FastAPI
from dotenv import load_dotenv
from src.auth.router import router as auth_router

load_dotenv()
app = FastAPI()
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
