from fastapi import APIRouter
from chatApi.models.thread import getThreads, getThreadById
from chatApi.api.thread import  get_thread, get_thread_by_id

router = APIRouter()

# @router.post("/thread/")
# def create_thread_endPoint(thread: ThreadCreate):
#     return create_thread(thread)

    
@router.get("/user/thread/{userId},{organizationId}")
def get_thread_endPoint(userId: str,organizationId: str):
    return get_thread(userId,organizationId)


@router.get("/thread/{userId},{organizationId},{threadId}")
def get_thread_by_id_endPoint(userId: str, organizationId: str, threadId: str):
    return get_thread_by_id(userId, organizationId, threadId)



    
    