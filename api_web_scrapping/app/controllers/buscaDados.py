from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from models.busca import Busca
routerBD = APIRouter()

class CorpoPesquisa(BaseModel):
    palavras_chaves: List[str]
    

@routerBD.post('/')
def buscarDados(request: CorpoPesquisa):
    busca = Busca()
    items = busca.busca_dados_relevantes(request.palavras_chaves)
    
    return items