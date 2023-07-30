from fastapi import APIRouter
from imsosorry import uwuify
from pydantic import BaseModel

class Uwu(BaseModel):
    text: str

router = APIRouter()

@router.post("/uwuify")
async def ancient_scrolls(text: Uwu):
    uwuified = uwuify(text.text)
    return uwuified