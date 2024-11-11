from pydantic import BaseModel

class ApiResponse(BaseModel):
    status: int
    details: dict
