from fastapi import FastAPI 
from reading.router import router as reading_router

app = FastAPI()

app.include_router(reading_router, prefix="/reading", tags=["reading"])

@app.get("/")
async def root():
    return {"message": "Welcome to the RAG-based Grading API"}