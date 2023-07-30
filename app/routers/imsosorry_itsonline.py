from fastapi import APIRouter
from imsosorry import uwuify
from model.datamodels import UwU
from random import uniform


router = APIRouter()


@router.post("/uwuify")
async def ancient_scrolls(uwu: UwU):
    params = {
        "high": uniform(0.7, 1.0),
        "medium": uniform(0.4, 0.7),
        "low": uniform(0.1, 0.4),
    }
    if uwu.uwu_meter in ("high", "medium", "low"):
        uwuified = uwuify(
            uwu.text,
            stutter_strength=params.get(uwu.uwu_meter),
            emoji_strength=params.get(uwu.uwu_meter),
            tilde_strength=params.get(uwu.uwu_meter),
        )
        return uwuified
    else:
        return {"Error": {"valid strengths": ["high", "medium", "low"]}}
