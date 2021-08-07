from starlette.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel
from mangum import Mangum
from typing import List, Dict, Optional, Union
from sqlalchemy.orm import Session
from datetime import datetime
import json
import os

comments= json.load(open("comments.json", "r"))

app = FastAPI(
    title="Comentários",
    version=0.1
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["x-apigateway-header", "Content-Type", "X-Amz-Date"],
)


@app.get("/health/")
def health() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}

@app.get("/comments/")
def get_all_comments() -> List[Dict[str, Union[float, int, str]]]:
    if response := comments:
        return response
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem comentários sendo feitos.",
    )

@app.get("/comments/{content_id}/")
def get_comments(content_id: int) -> Dict[str, Union[float, int, str]]:
    if response := list(
        filter(lambda i: i.get("content_id") == content_id, comments)
    )[0]:
        return response
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Não foram encontrados comentários sobre o conteúdo '{content_id}' ",
    )

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

handler = Mangum(app, debug=True, enable_lifespan=False, spec_version=3)