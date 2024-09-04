

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base

class Reservation(Base):
    __tablename__ = "reservations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))
    check_in_date = Column(DateTime)
    check_out_date = Column(DateTime)
    
    user = relationship("User")
    room = relationship("Room")
