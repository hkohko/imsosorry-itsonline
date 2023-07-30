import uvicorn
from fastapi import FastAPI
from routers import imsosorry_itsonline, welcome

app = FastAPI()

app.include_router(imsosorry_itsonline.router)
app.include_router(welcome.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=80)
