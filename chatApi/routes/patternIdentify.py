from fastapi import APIRouter
from chatApi.api.patternIdentify import find_placeholders
from chatApi.models.patternIdentify import PatternIdentify

router = APIRouter()

@router.post("/identify_pattern/")
async def identify_pattern(text: PatternIdentify):
    results= await find_placeholders(text.text)
    print(results)
    return results