from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession

from core.users import models, schemas, hashing
from core import utils


async def user_create(session: AsyncSession, user: schemas.UserRecordCreateRequest):
    user_uuid: str = utils.generate_uuid()
    user_password: str = hashing.get_password_hash(user.password)
    user_email: str = user.email
    user_create_date: datetime = datetime.now()
    user = models.User(
        uuid=user_uuid,
        password=user_password,
        email=user_email,
        create_date=user_create_date,
    )
    session.add(user)
    await session.commit()
    return user


async def users_read_all(session: AsyncSession):
    query = sqlalchemy.select(models.User)
    query_result = await session.execute(query)
    return query_result.scalars().all()


async def users_read_by_email(session: AsyncSession, email: str):
    query = sqlalchemy.select(models.User).where(models.User.email == email)
    query_result = await session.execute(query)
    return query_result.scalars().one_or_none()
