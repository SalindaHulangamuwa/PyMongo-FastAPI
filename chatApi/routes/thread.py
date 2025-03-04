from fastapi import APIRouter
from chatApi.models.thread import ThreadCreate
from chatApi.api.thread import create_thread, get_thread, get_thread_by_id

router = APIRouter()

@router.post("/thread/")
def create_thread_endPoint(thread: ThreadCreate):
    return create_thread(thread)

    
@router.get("/user/thread/{userId}")
def get_thread_endPoint(userId: str):
    return get_thread(userId)


@router.get("/thread/{threadId}")
def get_thread_by_id_endPoint(threadId: str):
    return get_thread_by_id(threadId)



    
    