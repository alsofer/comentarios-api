from starlette.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from mangum import Mangum
from typing import List
from sqlalchemy.orm import Session



app = FastAPI(
    title="Comentários",
    version=0.1,
    root_path="/production/"
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["x-apigateway-header", "Content-Type", "X-Amz-Date"],
)

@app.get('/healthcheck', name='HealthCheck da aplicação', tags=['HealthCheck'])
def healthcheck():
    return {"OK!"}

@app.get('/comment/list', name='Listar comentários', tags=['List'])
def list_comments():
    return {"Sample"}

@app.post('/comment/new', name='Adicionar um novo comentário', tags=['Add'])
def new_comment():
    return {"Sample"}

handler = Mangum(app, debug=True, enable_lifespan=False, spec_version=3)