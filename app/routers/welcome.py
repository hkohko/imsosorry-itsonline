from fastapi import APIRouter
from model.datamodels import Greetings

router = APIRouter()


@router.get("/")
async def greetings_heathen():
    return Greetings().greetings
