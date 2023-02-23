from fastapi import FastAPI

from ORM.base import create_database, stop_database

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.on_event("startup")
async def startup():
    await create_database()


@app.on_event("shutdown")
async def shutdown():
    await stop_database()
