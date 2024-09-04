

from pydantic import BaseModel
from datetime import datetime

class ReservationBase(BaseModel):
    user_id: int
    room_id: int
    check_in_date: datetime
    check_out_date: datetime

class ReservationCreate(ReservationBase):
    pass

class ReservationResponse(ReservationBase):
    id: int

    class Config:
        orm_mode = True
