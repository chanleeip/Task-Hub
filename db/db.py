import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String,TIMESTAMP,Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import ENUM
from models import Gender

Base=declarative_base()

class Users(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,autoincrement=True)
    uuid=Column(UUID(as_uuid=True),default=uuid.uuid4,autoincrement=False,primary_key=True)
    username=Column(String(30),nullable=False,unique=True)
    first_name=Column(String(30),nullable=False)
    last_name=Column(String(30),nullable=False)
    middle_name=Column(String(30),nullable=True)
    timestamp_created=Column(TIMESTAMP(timezone=False),default=datetime.now())
    gender=Column(ENUM(Gender),nullable=True)

