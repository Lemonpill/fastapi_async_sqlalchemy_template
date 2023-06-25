from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserRecordBase(BaseModel):
    email: str


class UserRecordCreateRequest(UserRecordBase):
    email: EmailStr
    password: str


class UserRecordPublic(UserRecordBase):
    uuid: str
    create_date: datetime

    class Config:
        orm_mode = True


class UserRecordFull(UserRecordPublic):
    id: int
    password: str

    class Config:
        orm_mode = True
