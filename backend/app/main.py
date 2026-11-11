from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .schemas import ScanRequest, ScanResponse
from .services.scam_detector import detect_scam
from .database.connection import initialize_database
from .database.models import save_scan, get_scan_history


app = FastAPI(
    title="ScamShield AI",
    description="Scam and phishing detection API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
def startup():
    initialize_database()


@app.get("/")
def home():
    return {
        "message": "ScamShield AI API is running",
        "status": "online"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/api/detect", response_model=ScanResponse)
def scan_content(request: ScanRequest):

    content = request.content.strip()

    if request.content_type == "url":
        if not content.startswith(("http://", "https://")):
            content = "http://" + content

    try:
        result = detect_scam(
            content,
            request.content_type
        )

        save_scan(
            content,
            request.content_type,
            result
        )

        return result

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="Detection failed"
        )


@app.get("/api/history")
def history():
    try:
        return get_scan_history()
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to retrieve scan history"
        )
