from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import APP_ENV, APP_NAME, CORS_ORIGINS, VERSION

app = FastAPI(title="OrgSession Status API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/status")
def get_status():
    return {
        "app_name": APP_NAME,
        "version": VERSION,
        "environment": APP_ENV,
        "status": "All systems operational",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
