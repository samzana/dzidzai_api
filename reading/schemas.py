from pydantic import BaseModel 
from typing import List

class ReadingRequest(BaseModel):
    passage: List[str]
    question: str 
    response: str 

class ReadingResponse(BaseModel):
    grade: str 
    feedback: str 
