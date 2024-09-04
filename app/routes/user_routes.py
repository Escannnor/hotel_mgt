

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.models.user import Users
from app.db.base import database
from app.services.user_service import create_user, get_user

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def register_user(user: UserCreate):
    # User creation logic here
    return user
