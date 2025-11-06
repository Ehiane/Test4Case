"""
Author: Ehiane Oigiagbe
Last Modified: November 5, 2025
Description:
---
    Configuration utilities for the application.
    Handles loading environment variables and setting default values.
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration class to manage environment variables."""

    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY", "")
    AI_MODEL = os.getenv("AI_MODEL", "Claude Sonnet 4")
    SANDBOX_TIMEOUT_SECONDS = int(os.getenv("SANDBOX_TIMEOUT_SECONDS", "6"))
    ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS", "*").split(",")  # CORS settings

config = Config()