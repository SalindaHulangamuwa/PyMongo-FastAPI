import uuid
from chatApi.db.dataBase import threads_collection

def create_thread_heading(threadHeading: str, userId: str):
    thread_id = str(uuid.uuid4())  # Generate a unique UUID for _id
    
    thread_data = {
        "_id": thread_id,
        "userId": userId,
        "threadHeading": threadHeading
    }
    
    result = threads_collection.insert_one(thread_data)
    
    return {"message": "Thread created successfully", "threadId": thread_id}
