from typing import List
from pydantic import BaseModel
from uuid import uuid4

class UserMetaData(BaseModel):
    userId: str
    organizationId: str
    policyIds: List[uuid4] = []
    evidenceIds: List[uuid4] = []
    hazardIds: List[uuid4] = []
    incidentIds: List[uuid4] = []