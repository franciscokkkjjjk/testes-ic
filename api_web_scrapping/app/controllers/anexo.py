from fastapi import APIRouter, Response
from bs4 import BeautifulSoup
from zipfile import ZipFile
from models.arquivo import Arquivo
import os
import requests

router = APIRouter(
    prefix='/anexo'
)

#TODO: tratar errors de arquivos

# endpoint responsavel por baixar e compactar os Anexo 1 e 2 na forma de pdf, e depois armazenar na maquina
@router.get('/download')
async def downloadAnexo(response: Response):
    r = requests
    arquivo = Arquivo()
    
    request_pagina = r.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
    
    if request_pagina.status_code != 200: 
        return {
            "mensagem": "Não foi possivel realizar a requisição na página destino.",
            "status_code_pagina_destino": request_pagina.status_code,
            "status_anexo": False
        } 
        
    html_text = request_pagina.text
    soup = BeautifulSoup(html_text, 'html.parser')
    text_body = soup.find('div', attrs={'class':'cover-richtext-tile tile-content'})
    list_area = text_body.find('ol')
    links_anexos = list_area.find_all('a', attrs={'target': '_blank'})
    
    lista_de_caminhos_anexo = []

    for link in links_anexos:
        url_anexo = link['href']
        caminho_absoluto_anexo = arquivo.download(url_anexo)  
        lista_de_caminhos_anexo.append(caminho_absoluto_anexo)
    arquivo.compactar(lista_de_caminhos_anexo, 'anexo_I_II')
    
    return {
        "status_anexo": True
    } 