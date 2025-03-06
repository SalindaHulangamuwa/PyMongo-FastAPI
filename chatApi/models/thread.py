from pydantic import BaseModel

class getThreads(BaseModel):
    userId: str
    organizationId: str

class getThreadById(BaseModel):
    userId: str
    organizationId: str
    threadId: str