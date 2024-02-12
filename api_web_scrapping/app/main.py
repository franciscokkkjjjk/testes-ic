from fastapi import FastAPI
from rotas import anexo, pesquisa

app = FastAPI()

app.include_router(router=anexo.routerAnexo)
app.include_router(router=pesquisa.routerPesquisa)

