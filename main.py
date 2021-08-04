import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum  # <---------- import Mangum library

app = FastAPI(title='Comentários')
handler = Mangum(app=app)

class Comment(BaseModel):
    email: str
    comment: str
    content_id: int

@app.get("/healthcheck")
def healthcheck():
    return {"OK!"}

@app.post("/comment/new")
async def new_comment(comment: Comment):
    return {"Comentário enviado com sucesso": comment}