# utils.py

from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

def get_non_field_error(erro_msg):
    return {"error": erro_msg}

def get_500_error():
    return get_non_field_error("Internal server error")

def get_500_response():
    return JSONResponse(get_500_error(), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = [{"field": e["loc"][-1], "error": e["msg"]} for e in exc.errors()]
    return JSONResponse(
        {"errors": errors},
        status_code=status.HTTP_400_BAD_REQUEST
    )
