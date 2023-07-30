from pydantic import BaseModel


class UwU(BaseModel):
    text: str
    uwu_meter: str = "medium"
