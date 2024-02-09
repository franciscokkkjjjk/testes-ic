from typing import Dict, Union, List
from fastapi import APIRouter
from models.arquivo import Arquivo
from pydantic import BaseModel
import pandas

routerED = APIRouter()

class paramsSubstituicao(BaseModel):
    pesquisa: str
    substitui: str

@routerED.get('/extrairTabelas/{nome_arquivo}')
async def extrairDados(nome_arquivo, paginas=None, paramsSubs: List[paramsSubstituicao] | paramsSubstituicao | None  = None):
    arq = Arquivo()
    lista_de_tabelas = arq.ler_pdf(nome_pdf=nome_arquivo, paginas=paginas)
    if len(lista_de_tabelas) > 0:
        lista_de_tabelas = pandas.concat(lista_de_tabelas)
    if len(lista_de_tabelas) == 0:
        return {
            'mensagem': 'Nenhuma tabela foi encontrada.'
        }
        
    if(paramsSubs):
            if(isinstance(paramsSubs, list)):
                for param in paramsSubs:
                    lista_de_tabelas = lista_de_tabelas.replace(param.pesquisa, param.substitui)
            else:
                lista_de_tabelas = lista_de_tabelas.replace(paramsSubs.pesquisa, paramsSubs.substitui)
                
    arq.converte_csv(nome_arquivo, lista_de_tabelas)
    return {True}