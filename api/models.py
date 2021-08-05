from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from .database import Base
from pydantic import BaseConfig

BaseConfig.arbitrary_types_allowed = True

class Comment(Base):
    __tablename__ = "comments"
    
    email = Column(String(55))
    comment = Column(String(255))
    content_id = Column(Integer, index=True, primary_key=True)