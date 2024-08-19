from fastapi import APIRouter, HTTPException 
from reading.services import grade_reading_response, grade_summary_response
from reading.schemas import ReadingRequest, ReadingResponse, SummaryRequest

router = APIRouter()

@router.post("/grade")
async def grade_reading(request: ReadingRequest):
    try:
        result = grade_reading_response(
            passage=request.passage,
            question=request.question,
            response=request.response
        )
        return ReadingResponse(
            grade=result["answer"],
            feedback=result["answer"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/summary")
async def grade_summary(request: SummaryRequest):
    try:
        result = grade_summary_response(
            passage=request.passage,
            question=request.question,
            response=request.response
        )
        return  ReadingResponse(
            grade=result["answer"],
            feedback=result["answer"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/reading")
async def read_reading():
    return {"message": "Welcome to the reading grading API"}
    