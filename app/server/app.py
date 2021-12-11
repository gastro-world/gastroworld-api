from fastapi import FastAPI
from .routes.destination import router as DestinationRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(DestinationRouter, tags=["Places"], prefix="/places")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message":"it works"}