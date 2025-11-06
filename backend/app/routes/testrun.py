"""
Route in charge of test running endpoints.
---
Authors: Ehiane Oigiagbe
Last Modified: November 5, 2025
"""

from fastapi import APIRouter
from app.models.test_models import RunTestsRequest, RunTestsResponse
from app.services.sandbox_service import run_pytest

router = APIRouter(prefix="/run-tests", tags=["test-runner"])

@router.post("", response_model=RunTestsResponse)
async def run_tests_endpoint(payload: RunTestsRequest) -> RunTestsResponse:
    """
    Endpoint to run tests against provided source code in a sandboxed environment.
    """

    # TODO: static code guards before executing
    return run_pytest(payload)
