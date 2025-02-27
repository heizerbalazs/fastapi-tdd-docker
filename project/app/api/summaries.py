# project/app/api/summaries.py

from fastapi import APIRouter, HTTPException
from typing import List

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.models.tortoise import SummarySchema

router = APIRouter()


@router.get("/", response_model=List[SummarySchema])
async def read_all_summaries() -> List[SummarySchema]:
    return await crud.get_all()


@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(id: int) -> SummarySchema:
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    return summary


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(pyload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(pyload)

    response_object = {"id": summary_id, "url": pyload.url}
    return response_object
