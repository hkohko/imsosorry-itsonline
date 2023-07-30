from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def greetings_heathen():
    return "Welcome, chosen one."