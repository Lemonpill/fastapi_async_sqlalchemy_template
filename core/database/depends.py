# Dependency
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.session import async_session, engine
from core.database.base import Base


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
