from sqlalchemy import Column, String, Integer, DateTime, Boolean

from core.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    date = Column(DateTime)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
