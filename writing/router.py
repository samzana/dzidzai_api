from fastapi import APIRouter, HTTPException
from writing.schemas import FreeWritingRequest, GuidedWritingRequest
from writing.services import grade_free_composition_response, grade_guided_composition_response


router = APIRouter()

@router.post("/free_compositions")
async def grade_free_compositions(request: FreeWritingRequest):
    try:
        result = grade_free_composition_response(
            prompt=request.prompt,
            composition_type=request.type,
            response=request.response
        )
        return result["answer"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/guided_compositions")
async def grade_guided_compositions(request: GuidedWritingRequest):
    try:
        result = grade_guided_composition_response(
            prompt=request.prompt,
            composition_type=request.type,
            response=request.response
        )
        return result["answer"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
   
    

