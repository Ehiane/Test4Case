"""
    AI service module to generate test cases using Claude API.
---
Author: Ehiane Oigiagbe
Last Modified: November 5, 2025
"""

from typing import Dict, List
from app.models.test_models import GenerateTestsRequest, GenerateTestsResponse, TestCase


# in the real version, call Claude here. but for now, return a deterministic stub so the UI works. 
def generate_tests(req: GenerateTestsRequest) -> GenerateTestsResponse:

    example_test = TestCase(
        name="test_example_function",
        body="""
def test_example_runs():
    # Arrange
    # (import user module if needed)
    assert True
""".strip(),
        explanation="Sanity test to show the framework is wired correctly."
    )

    tests_code = f"""
    import pytest 
    
    {example_test.body}""".strip()

    return GenerateTestsResponse(
        framework=req.style or "pytest",
        tests_code=tests_code,
        cases=[example_test],
        metadata={"note": "AI stubbed response; wire Claude next."}
    )


