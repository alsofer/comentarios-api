from . import routes
from . import database
from fastapi import FastAPI
from .database import conn


app = FastAPI(title='Comentários API', description='API para envio de comentários online', version='0.1')
app.include_router(routes.router_comment)
 

@app.on_event("startup")
async def startup():
    if conn.is_closed():
        conn.connect()
 
@app.on_event("shutdown")
async def shutdown():
    print("Closing...")
    if not conn.is_closed():
        conn.close()