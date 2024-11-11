from apps.user.schemas import SignupIn
from sqlalchemy.orm import Session
from apps.user.models import User
from error.errorutil import get_non_field_error
from fastapi import status
from common_util import get_api_response

def is_email_exist(email, db: Session) -> bool:
        return db.query(User).filter(User.email==email).first() is not None

def handle_email_exist_error():
    details = get_non_field_error("Email already exist")

    return get_api_response(details, status.HTTP_409_CONFLICT)

def handle_signup_success_response(email):
    return get_api_response({"email": email}, status.HTTP_201_CREATED)  

def create_user(signup_data, db):
    user = User(username=signup_data.email, email=signup_data.email)
    user.set_password(signup_data.password)
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def signup(signup_data: SignupIn, db: Session):
    if is_email_exist(signup_data.email, db):

        return handle_email_exist_error()
    
    user = create_user(signup_data, db)

    return handle_signup_success_response(user.email)
    