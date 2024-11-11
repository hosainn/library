from fastapi import FastAPI
from apps.user.routers import router as user_router
from database import get_db, engine
from apps.user import models
from fastapi.exceptions import RequestValidationError
from error.errorutil import validation_exception_handler 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

@app.get("/")
def index():
    return {"Message": "Hello World"}