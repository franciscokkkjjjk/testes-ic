from fastapi import APIRouter
from models.arquivo import Arquivo

routerED = APIRouter()

@routerED.get('/extrairTabelas/{nome_arquivo}')
async def extrairDados(nome_arquivo, paginas):
    arq = Arquivo()
    arq.converte_csv(nome_arquivo, nome_arquivo, paginas=paginas)
    return {True}