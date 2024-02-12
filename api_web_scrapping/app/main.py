from fastapi import FastAPI
from rotas import anexo, pesquisa
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router=anexo.routerAnexo)
app.include_router(router=pesquisa.routerPesquisa)
origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)