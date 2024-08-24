from pydantic import BaseModel
from typing import List

class GuidedWritingRequest(BaseModel):
    prompt: List[str]
    type: str
    response: str

class FreeWritingRequest(BaseModel):
    prompt: str
    type: str
    response: str