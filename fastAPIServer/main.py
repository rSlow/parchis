from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from ORM.base import create_database, stop_database
from routes import api_router, websocket_router

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
app.include_router(websocket_router)


@app.middleware("http")
async def middleware(request: Request, call_next):
    return await call_next(request)


@app.on_event("startup")
async def startup():
    await create_database()


@app.on_event("shutdown")
async def shutdown():
    await stop_database()
