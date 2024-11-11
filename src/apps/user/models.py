import uuid
import bcrypt
from sqlalchemy import Column, BigInteger, String, Integer

from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(36), nullable=False, unique=True, default=lambda: str(uuid.uuid4()), index=True)
    username = Column(String(150), nullable=False, unique=True)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(60), nullable=False)

    def set_password(self, password: str) -> None:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.password = hashed_password

    def check_password(self, password: str) -> bool:
        return bcrypt.hashpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def __str__(self):
        return self.username




