from fastapi import FastAPI
from rotas import anexo

app = FastAPI()

app.include_router(router=anexo.router)

