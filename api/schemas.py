from pydantic import BaseModel

class CommentsBaseSchema(BaseModel):
    email: str
    comment: str

class CommentsSchema(CommentsBaseSchema):
    email: str
    comment: str
    comment_unique_id: int

class CreateCommentsSchema(CommentsBaseSchema):
    email: str
    comment: str