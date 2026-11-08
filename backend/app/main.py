from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import AnalyzeRequest
from app.services.detector import analyze_text
from app.database.db import (
    initialize_database,
    save_scan,
    get_history,
    get_dashboard_stats
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    yield

app = FastAPI(
    title="ScamCall Shield AI",
    description="Scam message and call transcript risk analysis API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",
        "http://127.0.0.1:8501"
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"]
)

@app.get("/")
def home():
    return {
        "message": "ScamCall Shield AI backend is running"
    }

@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "service": "ScamCall Shield AI"
    }

@app.post("/api/analyze/message")
def analyze_message(request: AnalyzeRequest):
    result = analyze_text(request.text)
    save_scan("message", result)
    return result

@app.post("/api/analyze/call")
def analyze_call(request: AnalyzeRequest):
    result = analyze_text(request.text)
    save_scan("call", result)
    return result

@app.get("/api/history")
def history():
    return get_history()

@app.get("/api/dashboard")
def dashboard():
    return get_dashboard_stats()
