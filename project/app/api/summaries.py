# project/app/api/summaries.py

from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema

router = APIRouter()

@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(pyload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(pyload)

    response_object = {
        "id": summary_id,
        "url": pyload.url
    }
    return response_object

