from typing import List
from reading.schemas import ReadingResponse
from common.rag import create_rag_chain
from common.prompts import READING_PROMPT

rag_chain = create_rag_chain("reading", READING_PROMPT)

def grade_reading_response(passage: List[str], question: str, response: str):
    combined_passage = " ".join(passage)
    input_context = f"passage: {combined_passage}\n\nquestion: {question}\n\nresponse: {response}"
    #structured_rag_chain = rag_chain.with_structured_output(ReadingResponse)
    return rag_chain.invoke({"input": input_context})