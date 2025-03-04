from typing import List
from pydantic import BaseModel, Field

class UserMetaData(BaseModel):
    userId: str = Field(..., alias="_id") 
    organizationId: str
    policyIds: List[str] = []
    evidenceIds: List[str] = []
    hazardIds: List[str] = []
    incidentIds: List[str] = []

    class Config:
        allow_population_by_field_name = True 
