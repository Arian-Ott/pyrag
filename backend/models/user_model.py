from backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, UUID, DateTime
from uuid import uuid4
from datetime import datetime


class UserModel(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(32), unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=datetime.now)
