"""
    Data models for testing purposes using Pydantic.
---
Author: Ehiane Oigiagbe
Last Modified: November 5, 2025
"""

from pydantic import BaseModel, Field, StringConstraints
from typing import Optional, List, Dict, Any, Literal, Annotated

Language = Literal["python"] # TODO: expandable for more languages in the future

# Field(..., description="..."), the ""..."" in the first argument indicates a required field.


class GenerateTestsRequest(BaseModel):
    """
    Request model for generating tests.
    """

    code: Annotated[str, StringConstraints(min_length=1)] = Field(..., description="The source code to generate tests for.")
    language: Language = Field("python", description="The programming language of the source code.")
    # prefer a concrete Literal when providing a default; not Optional unless you want to allow None
    style: Literal["pytest", "unittest"] = Field("pytest", description="The testing style to use.")
    goals: Optional[List[str]] = Field(default=None, description="Learning goals or hints.")


class TestCase(BaseModel):
    """
    Model representing a single test case.
    """
    name: str = Field(..., description="The name of the test case.")
    body: str = Field(..., description="The raw test code for one test function/method.")
    explanation: str = Field(..., description="Explanation of what the test case is validating.")


class GenerateTestsResponse(BaseModel):
    """
    Response model for generated tests.
    """
    framework: Literal["pytest", "unittest"] = Field(..., description="The testing framework used (e.g., pytest, unittest).")
    tests_code: str = Field(..., description="The complete generated test code.")
    cases: List[TestCase] = Field(..., description="List of generated test cases with explanations.")
    # avoid a shared mutable default — use default_factory
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata if needed")


class RunTestsRequest(BaseModel):
    """
    Request model for running tests.
    """
    code: Annotated[str, StringConstraints(min_length=1)] = Field(..., description="The source code to be tested.")
    tests_code: Annotated[str, StringConstraints(min_length=1)] = Field(..., description="The test code to run against the source code.")
    runner: Literal["pytest"] = Field("pytest", description="The test runner to use. Currently only pytest is supported.")
    timeout_sec: int = Field(6, description="Max seconds to run tests")

    class Config:
        json_schema_extra = {
            "example": {
                "code": "def add(a, b):\n    return a + b",
                "tests_code": "import pytest\n\ndef test_add():\n    assert add(2, 3) == 5",
                "runner": "pytest",
                "timeout_sec": 6
            }
        }


class TestResult(BaseModel):
    """
    Model representing the result of a single test case.
    """
    name: str = Field(..., description="The name of the test case.")
    status: Literal["passed", "failed", "error", "skipped"] = Field(..., description="The result status of the test case.")
    message: Optional[str] = Field(None, description="Optional message (error/traceback/etc.)")


class RunTestsResponse(BaseModel):
    """
    Response model for test run results.
    """
    passed: int = Field(..., description="Number of tests that passed.")
    failed: int = Field(..., description="Number of tests that failed.")
    errors: int = Field(..., description="Number of tests that encountered errors.")
    skipped: int = Field(..., description="Number of tests that were skipped.")
    results: List[TestResult] = Field(..., description="Detailed results for each test case.")
    raw_output: str = Field(..., description="Raw output from the test runner.")


class SaveSessionRequest(BaseModel):
    """
    Request model for saving a session.
    """
    code: str = Field(..., description="The source code to be saved.")
    tests_code: str = Field(..., description="The test code to be saved.")
    run_summary: Optional[RunTestsResponse] = Field(None, description="Summary of the last test run.")


class SaveSessionResponse(BaseModel):
    """
    Response model for saving a session.
    """
    session_id: str = Field(..., description="Unique identifier for the saved session.")
    stored: bool = Field(True, description="Indicates whether the session data is stored.")