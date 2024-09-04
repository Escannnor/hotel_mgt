

from sqlalchemy import Column, String, Boolean, Integer
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="GUEST")  # Roles: Admin, Receptionist, Housekeeping, Guest
    is_active = Column(Boolean, default=True)
