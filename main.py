from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from words import BRAINROT
import random

app = FastAPI()

# Armazenamento em memória
SERVER_REPORTS = {}

# CORS para Roblox
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API online!"}

@app.post("/api/report")
async def report(request: Request):
    data = await request.json()
    server_id = data.get("server_id", "unknown")
    SERVER_REPORTS[server_id] = {
        "place_id": data.get("place_id"),
        "models": data.get("models"),
        "timestamp": data.get("timestamp"),
    }
    return {"message": f"Data received from server {server_id}!"}

@app.get("/api/data")
async def get_data():
    return {"servers": SERVER_REPORTS}

@app.get("/api/brainrot/random")
async def get_random_brainrot():
    term = random.choice(list(BRAINROT.keys()))
    return {
        "term": term,
        "definition": BRAINROT[term]["definition"],
        "example": BRAINROT[term]["example"]
    }
