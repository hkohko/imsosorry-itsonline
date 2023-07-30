from fastapi import APIRouter
from imsosorry import uwuify
from pydantic import BaseModel
from random import random


class UwU(BaseModel):
    text: str
    cultured: str = "medium"


router = APIRouter()


@router.post("/uwuify")
async def ancient_scrolls(text: UwU, culture: str):
    params = {
        "high": random(0.7, 1.0),
        "medium": random(0.4, 0.7),
        "low": random(0.1, 0.4),
    }
    if culture in ("high", "medium", "low"):
        uwuified = uwuify(
            text.text,
            stutter_strength=params.get(culture),
            emoji_strength=params.get(culture),
            tilde_strength=params.get(culture),
        )
        return uwuified
    else:
        return {"Error": {"valid strengths": ["high", "medium", "low"]}}
