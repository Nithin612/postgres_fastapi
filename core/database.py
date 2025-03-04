from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

# Create an async engine
engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)

# Create a session factory
AsyncSessionLocal = sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)


# Dependency Injection for DB Session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
