from pydantic import BaseModel


class UwU(BaseModel):
    text: str
    uwu_meter: str = "medium"


class Greetings(BaseModel):
    greetings: str = "Welcome, chosen one."
