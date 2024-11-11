from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from starlette import status
from .schemas import SignupIn
from sqlalchemy.orm import Session
from database import get_db
from apps.user.controller.user_auth import signup
from error.errorutil import get_500_response

router = APIRouter()

@router.post("/signup/", tags=["user signup"])
def user_signup(signup_data: SignupIn, db: Session = Depends(get_db)):
    try:
        api_response = signup(signup_data, db)
        return JSONResponse(api_response.details, status_code=api_response.status)
    except Exception as err:
        print(str(err))
        return get_500_response()