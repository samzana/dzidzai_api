from pydantic import BaseModel 
from typing import List

class ReadingRequest(BaseModel):
    passage: List[str]
    question: str 
    response: str 

class ReadingResponse(BaseModel):
    grade: str 
    feedback: str 


class SummaryRequest(BaseModel):
    passage: List[str]
    question: List[str]
    response: str