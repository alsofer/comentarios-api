from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum  # <---------- import Mangum library
app = FastAPI(title='Comentários')

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["x-apigateway-header", "Content-Type", "X-Amz-Date"],
)

class Comment(BaseModel):
    email: str
    comment: str
    content_id: int

@app.get('/healthcheck', name='HealthCheck da aplicação', tags=['HealthCheck'])
def healthcheck():
    return {"OK!"}

@app.post('/comment/new', name='Adicionar um novo comentário', tags=['Add'])
async def new_comment(comment: Comment):
    return {"Comentário enviado com sucesso": comment}

handler = Mangum(app, debug=True, enable_lifespan=False, spec_version=3)