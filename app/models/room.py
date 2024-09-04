

from sqlalchemy import Column, String, Integer, Float, Boolean
from app.db.base import Base

class Room(Base):
    __tablename__ = "rooms"
    
    id = Column(Integer, primary_key=True, index=True)
    room_number = Column(String, unique=True, index=True)
    room_type = Column(String)  # Room Types: Standard, Double, Suite
    price = Column(Float)
    is_available = Column(Boolean, default=True)
    description = Column(String)
