from starlette.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from mangum import Mangum
from typing import List
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Comentários')

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["x-apigateway-header", "Content-Type", "X-Amz-Date"],
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/healthcheck', name='HealthCheck da aplicação', tags=['HealthCheck'])
def healthcheck():
    return {"OK!"}

@app.get('/comment/list', response_model=schemas.Comment, name='Listar comentários', tags=['List'])
def list_comments(db: Session = Depends(get_db)):
    comment = db.query(models.Comment).all()
    return comment

@app.post('/comment/new', response_model=schemas.Comment, name='Adicionar um novo comentário', tags=['Add'])
def new_comment(comment: schemas.Comment, db: Session = Depends(get_db)):
    return crud.new_comment(db=db, comment=comment)

handler = Mangum(app, debug=True, enable_lifespan=False, spec_version=3)