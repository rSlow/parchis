from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ORM.base import create_database, stop_database
from routes import api_router

app = FastAPI()

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
