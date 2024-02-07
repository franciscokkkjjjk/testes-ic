from fastapi import APIRouter, Response
from bs4 import BeautifulSoup
import os
import requests

router = APIRouter(
    prefix='/anexo'
)

default_path_download = os.path.abspath('.') + '/arquivos/'

# endpoint responsavel por baixar os Anexo 1 e 2 na forma de pdf, e depois armazenar na maquina
@router.get('/download')
async def downloadAnexo(response: Response):
    r = requests
    request_pagina = r.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
    if request_pagina.status_code != 200: 
        return {
            "mensagem": "Não foi possivel realizar a requisição na página destino.",
            "status_code_pagina_destino": request_pagina.status_code
        } 
    html_text = request_pagina.text
    soup = BeautifulSoup(html_text, 'html.parser')
    text_body = soup.find('div', attrs={'class':'cover-richtext-tile tile-content'})
    list_area = text_body.find('ol')
    links_anexos = list_area.find_all('a', attrs={'target': '_blank'})
    for link in links_anexos:
        url_anexo = link['href']
        request_anexo = r.get(url_anexo)
        anexo_path = os.path.join(default_path_download, os.path.basename(url_anexo))
        with open(anexo_path, 'wb') as file:
            file.write(request_anexo.content)
    return 