from fastapi import HTTPException
from chatApi.db.dataBase import users_collection, threads_collection
from chatApi.models.thread import ThreadCreate
import uuid


def create_thread(thread: ThreadCreate):
    user=users_collection.find_one({"userId": thread.userId})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    threadData = {
        "threadId": str(uuid.uuid4()),
        "userId": thread.userId,
        "threadHeading": thread.threadHeading,
    }
    threads_collection.insert_one(threadData)
    return {"message": "Thread created successfully", "threadId": threadData["threadId"]}



def get_thread(userId: str):
    threads=threads_collection.find_one({"userId": userId},{"_id":0,"threadId":1,"threadHeading":1})
    if not threads:
        raise HTTPException(status_code=404, detail="Thread not found")
    
    thread_list=list(threads)
    return {"threads": thread_list}



def get_thread_by_id(threadId: str):
    thread = threads_collection.find_one({"threadId": threadId}, {"_id": 0})  #First, find the query by threadId, and then project it. Setting _id=0 means the default _id is ignored.
    if not thread:
        raise HTTPException(status_code=404, detail="Thread not found")

    return thread