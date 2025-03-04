from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from schemas.user import UserCreate, UserResponse
from services.user_service import create_user, get_users

router = APIRouter()


@router.post("/", response_model=UserResponse)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)


@router.get("/", response_model=list[UserResponse])
async def list_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)
