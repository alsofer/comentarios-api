from datetime import date
from pydantic import BaseModel

class Comment(BaseModel):
    email: str
    comment: str
    content_id: int

    class Config:
        orm_mode = True

class NewComment(BaseModel):
    pass