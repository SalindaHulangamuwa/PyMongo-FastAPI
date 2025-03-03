from pydantic import BaseModel

class ThreadCreate(BaseModel):
    userId: str
    threadHeading: str