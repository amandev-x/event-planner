from fastapi import APIRouter, Body, status, HTTPException
from models.events import Event 
from typing import List

event_router = APIRouter(
    tags=["Events"]
)

events = []
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events():
    if not events:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event list is empty. Please add event to get it."
        )
    else:
        return events