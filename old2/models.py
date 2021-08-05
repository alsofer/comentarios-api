from typing import Any, List, Optional
from .Base import BaseModel
from pydantic.utils import GetterDict
from peewee import *

class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res

class Comment(BaseModel):
    email = CharField(max_length=40)
    comment = CharField(max_length=40)
    content_id = SmallIntegerField()
 
    class Meta:
        db_table = 'comments'
    
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


async def new_comment(email: str, comment: str, content_id: int):
    comment_object = Comment(
        email=email,
        comment=comment,
        content_id=content_id
    )
    comment_object.save()
    return comment_object

