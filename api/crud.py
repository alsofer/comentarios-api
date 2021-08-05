from sqlalchemy.orm import Session
from . import models, schemas

def list_comments(db: Session):
    comment = db.query(models.Comment).all()
    return comment

def new_comment(db: Session, comment: schemas.Comment):
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment