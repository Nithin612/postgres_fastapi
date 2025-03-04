# from fastapi import APIRouter, Depends
# from sqlalchemy.ext.asyncio import AsyncSession
# from core.database import get_db
# from schemas.user import UserCreate, UserResponse
# from services.user_service import create_user, get_users
#
# router = APIRouter()
#
#
# @router.post("/", response_model=UserResponse)
# async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
#     return await create_user(db, user)
#
#
# @router.get("/", response_model=list[UserResponse])
# async def list_users(db: AsyncSession = Depends(get_db)):
#     return await get_users(db)

from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.database import engine
from models.base import Base
from api.v1.endpoints.users import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # ✅ Auto-create tables
    yield  # ✅ App Starts
    await engine.dispose()  # ✅ Closes DB connection on shutdown

# ✅ Create FastAPI App with Docs
app = FastAPI(
    title="FastAPI PostgreSQL App",
    description="API documentation for our FastAPI project",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc UI
    openapi_url="/openapi.json"  # OpenAPI Schema
)

# ✅ Include API Routers
app.include_router(user_router, prefix="/api/v1/users", tags=["Users"])


@app.get("/")
async def root():
    return {"message": "FastAPI with PostgreSQL!"}
