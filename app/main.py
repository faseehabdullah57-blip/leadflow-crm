
from datetime import datetime, timezone

from fastapi import FastAPI


# Create our FastAPI application
app = FastAPI(
    title="LeadFlow CRM API",
    description="Backend for our AI-powered CRM platform",
    version="0.1.0"
)


# First API endpoint
@app.get("/health", tags=["System"])
def health_check():

    return {
        "status": "ok",
        "service": "leadflow-crm",
        "version": app.version,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
