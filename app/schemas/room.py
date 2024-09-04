

from pydantic import BaseModel

class RoomBase(BaseModel):
    room_number: str
    room_type: str
    price: float
    description: str

class RoomCreate(RoomBase):
    pass

class RoomResponse(RoomBase):
    id: int
    is_available: bool

    class Config:
        orm_mode = True
