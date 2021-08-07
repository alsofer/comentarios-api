from sqlalchemy import Column, Integer, String
from .database import Base

class ContentId1(Base):
    __tablename__ = "contentid1"

    email = Column(String(55), index=True)
    comment = Column(String(255))
    comment_unique_id = Column(Integer, primary_key=True, index=True)

class ContentId2(Base):
    __tablename__ = "contentid2"

    email = Column(String(55), index=True)
    comment = Column(String(255))
    comment_unique_id = Column(Integer, primary_key=True, index=True)