from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from .database import Base

class Comment(Base):
    __tablename__= "comments"
    
    email = Column(String(55))
    comment = Column(String(255))
    content_id = Column(Integer, index=True, primary_key=True)