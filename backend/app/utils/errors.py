"""
Author: Ehiane Oigiagbe
Last Modified: November 5, 2025
Description:
---
    Custom error classes for handling specific HTTP exceptions in FastAPI.
"""
from fastapi import HTTPException, status

class BadRequest(HTTPException):
    def __init__(self, detail: str = "Invalid request"):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail) # 422 is more appropriate for validation errors


class UnsafeCode(HTTPException):
    def __init__(self, detail: str = "Disallowed or unsafe code detected"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


class SandboxError(HTTPException):
    def __init__(self, detail: str = "Sandbox execution failed"):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)


class TimeoutError(HTTPException):
    def __init__(self, detail: str = "Code execution timed out"):
        super().__init__(status_code=status.HTTP_504_GATEWAY_TIMEOUT, detail=detail)


class ExternalAPIError(HTTPException):
    def __init__(self, detail: str = "External API request failed"):
        super().__init__(status_code=status.HTTP_502_BAD_GATEWAY, detail=detail)


class ResourceNotFound(HTTPException):
    def __init__(self, detail: str = "Requested resource not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class UnauthorizedAccess(HTTPException):
    def __init__(self, detail: str = "Unauthorized access"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


class ConflictError(HTTPException):
    def __init__(self, detail: str = "Resource conflict occurred"):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)   


class InternalServerError(HTTPException):
    def __init__(self, detail: str = "Internal server error"):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)


class ServiceUnavailable(HTTPException):
    def __init__(self, detail: str = "Service is currently unavailable"):
        super().__init__(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=detail)    