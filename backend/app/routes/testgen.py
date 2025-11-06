"""
    Route in charge of test generation endpoints.
---
Author: Ehiane Oigiagbe
Last Modified: November 5, 2025
"""

from fastapi import APIRouter
from app.models.test_models import GenerateTestsRequest, GenerateTestsResponse
from app.services.ai_service import generate_tests

router = APIRouter(prefix="/generate-tests", tags=["test-generation"])

@router.post("", response_model=GenerateTestsResponse)
async def generate_tests_endpoint(payload: GenerateTestsRequest) -> GenerateTestsResponse:
    """
    Endpoint to generate tests for given source code using AI.
    """

    # TODO: add safety checks here
    response = generate_tests(payload)
    return response

