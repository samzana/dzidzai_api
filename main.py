from fastapi import FastAPI 
from reading.router import router as reading_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  
    "http://127.0.0.1:3000",  
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

app.include_router(reading_router, prefix="/reading", tags=["reading"])

@app.get("/")
async def root():
    return {"message": "Welcome to the RAG-based Grading API"}