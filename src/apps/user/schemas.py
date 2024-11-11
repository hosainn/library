from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator

class SignupOut(BaseModel):
    email: EmailStr


class SignupIn(BaseModel):
    email: EmailStr
    password: str = Field(min_length=3, max_length=150)
    retype_password: str

    @field_validator("password")
    @classmethod
    def password_must_be_strong(cls, val: str):
        if "1" not in val:
            return ValueError("Must be strong")
        return val
    
    @model_validator(mode='after')
    def check_password_match(self):
        if self.password != self.retype_password:
            raise ValueError("Password do not match")
        return self
    


