"""
    Main application entry point for the Test4Case backend.
--- 
Author: Ehiane Oigiagbe
Last Modified: November 5, 2025
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import testrun, testgen, session
from app.utils.config import Config
import logging


logging.basicConfig(level=logging.INFO)
app = FastAPI(title="Test4Case Backend", version="0.1.0")
ALLOW_ORIGINS = Config.ALLOW_ORIGINS

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in ALLOW_ORIGINS if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
@app.get("/health", tags=["health"])

def health():
    return {"status": "ok"}

app.include_router(testrun.router)
app.include_router(testgen.router)
app.include_router(session.router)