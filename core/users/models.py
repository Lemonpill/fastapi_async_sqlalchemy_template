from sqlalchemy import Column, Integer, DateTime, String, func

from core.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    uuid = Column(String)
    password = Column(String)
    email = Column(String)
    create_date = Column(DateTime, server_default=func.now())

    # required in order to access columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}
