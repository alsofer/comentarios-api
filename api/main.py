## Dependências ##
from starlette.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.openapi.utils import get_openapi
import pydantic
from mangum import Mangum
from typing import Generator, List, Dict, Optional, Union
from sqlalchemy.orm import Session
from datetime import datetime
from .schemas import CommentsBaseSchema, CreateCommentsSchema, CommentsSchema
from .crud import create_comment_content_id_1, create_comment_content_id_2, retrieve_all_content_id_1, retrieve_all_content_id_2
from .database import Base, SessionLocal, engine
import json
import os
import re

Base.metadata.create_all(bind=engine)
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

################ Variáveis ################
app = FastAPI(
    title="Comentários API",
    version=0.1,
    root_path="/api"
    )


################ CORS ################
app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["x-apigateway-header", "Content-Type", "X-Amz-Date"],
)


################  Rotas ################
@app.get("/health", name='healthcheck')
def health() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}

@app.get("/comment/list/1", name='listar comentários sobre o conteúdo 1', status_code=status.HTTP_200_OK,)
def get_comments_content_1(
    db: Session = Depends(get_db)) -> Generator:
    if result := retrieve_all_content_id_1(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem comentários no momento.",
    )

@app.get("/comment/list/2", name='listar comentários sobre o conteúdo 2', status_code=status.HTTP_200_OK,)
def get_comments_content_2(
    db: Session = Depends(get_db)) -> Generator:
    if result := retrieve_all_content_id_2(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem comentários no momento.",
    )

@app.post("/comment/new/1", name='enviar comentário sobre o conteúdo 1', status_code=status.HTTP_201_CREATED,)
def post_comment_content_id1(
    comment: CreateCommentsSchema,
    db: Session = Depends(get_db)):
    if result := create_comment_content_id_1(db, comment):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )

@app.post("/comment/new/2", name='enviar comentário sobre o conteúdo 2', status_code=status.HTTP_201_CREATED,)
def post_comment_content_id2(
    comment: CreateCommentsSchema,
    db: Session = Depends(get_db)):
    if result := create_comment_content_id_2(db, comment):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )


################ Documentação #################
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Comentários API",
        version="0.1",
        description="Api de comentários online",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://upload.wikimedia.org/wikipedia/pt/2/22/Logotipo_da_Rede_Globo.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


################ Handler para AWS Lambda Function #################
handler = Mangum(app, debug=True, enable_lifespan=False, spec_version=3)