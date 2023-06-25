from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(
    "postgresql+asyncpg://postgres:0585805055@localhost:5432/fastapi-receipt-backend",
    # echo=True,
)

# expire_on_commit=False will prevent attributes from being expired
# after commit.
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
