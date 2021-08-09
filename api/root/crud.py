from typing import Generator

from sqlalchemy.orm import Session
from .models import ContentId1, ContentId2
from .schemas import CommentsSchema, CreateCommentsSchema

contentid1 = ContentId1
contentid2 = ContentId2

def create_comment_content_id_1(
    db: Session, contentid1: CreateCommentsSchema
):
    new_comment = ContentId1(**contentid1.dict())
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def create_comment_content_id_2(
    db: Session, contentid2: CreateCommentsSchema
):
    new_comment = ContentId2(**contentid2.dict())
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def retrieve_all_content_id_1(db: Session) -> Generator:
    return db.query(contentid1).all()

def retrieve_all_content_id_2(db: Session) -> Generator:
    return db.query(contentid2).all()