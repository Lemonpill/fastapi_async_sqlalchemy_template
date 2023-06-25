from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from core.database.config import settings

engine = create_async_engine(
    settings.SQLALCHEMY_URL
    # echo=True,
)

# expire_on_commit=False will prevent attributes from being expired
# after commit.
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
