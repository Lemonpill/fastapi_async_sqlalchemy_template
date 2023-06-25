from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.depends import get_session
from core.users import schemas, service

router = APIRouter(prefix="/users")


@router.get("/", response_model=list[schemas.UserRecordPublic])
async def users_read_all(session: AsyncSession = Depends(get_session)):
    return await service.users_read_all(session=session)


@router.post("/", response_model=schemas.UserRecordPublic)
async def user_create(
    user: schemas.UserRecordCreateRequest, session: AsyncSession = Depends(get_session)
):
    if await service.users_read_by_email(session=session, email=user.email):
        raise HTTPException(400, "Email already exists!")
    return await service.user_create(session=session, user=user)
