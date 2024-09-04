from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String, default="GUEST")  # Admin, Receptionist, Housekeeping, Guest
    is_active = Column(Boolean, default=True)
