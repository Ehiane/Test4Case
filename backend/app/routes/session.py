"""
    Route in charge of session management endpoints.
---
Author: Ehiane Oigiagbe
Last Modified: November 5, 2025
"""

import logging
import uuid
from fastapi import APIRouter
from app.models.test_models import SaveSessionRequest, SaveSessionResponse


router = APIRouter(prefix="/save-session", tags=["session"])

# MVP: we return a fake session ID for now. later we can persist to a DB. (SQLite/Mongo)

@router.post("", response_model=SaveSessionResponse)
async def save_session_endpoint(payload: SaveSessionRequest) -> SaveSessionResponse:
    """
    Endpoint to save a user session.
    """
    session_id = str(uuid.uuid4())
    logging.info(f"Session saved with ID: {session_id}")
    return SaveSessionResponse(session_id=session_id, stored=True)