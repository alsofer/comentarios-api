from datetime import date
from .database import Base

class Comment(Base):
    __tablename__ = "comments"
    email: str
    comment: str
    content_id: int

    class Config:
        orm_mode = True