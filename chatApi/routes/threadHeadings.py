from fastapi import APIRouter
from chatApi.api.threadHeading import create_thread_heading

router=APIRouter()

@router.post("/threadHeadings")
async def create_thread_heading_endPoint(threadHeading: str, userId: str):
    return create_thread_heading(threadHeading, userId)