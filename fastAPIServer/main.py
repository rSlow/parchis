from fastapi import FastAPI

from ORM.base import create_database, stop_database
from routes import api_router

app = FastAPI()
app.include_router(api_router)


@app.get("/")
async def start():
    return True


@app.on_event("startup")
async def startup():
    await create_database()


@app.on_event("shutdown")
async def shutdown():
    await stop_database()
