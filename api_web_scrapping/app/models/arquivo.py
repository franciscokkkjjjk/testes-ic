from typing import Union
from zipfile import ZipFile
import os
import requests
class Arquivo:
    caminho_padrao_arquivo = os.path.abspath('.') + '/arquivos/'     
        
    def download(self, url: str) -> Union[str, None]: 
        request_anexo = requests.get(url)
        anexo_path = os.path.join(self.caminho_padrao_arquivo, os.path.basename(url))
        with open(anexo_path, 'wb') as file:
            file.write(request_anexo.content)
        return anexo_path

    def compactar(self, caminho_arquivo: Union[str, list], nome_do_zip: str) -> None:
        with ZipFile(self.caminho_padrao_arquivo + f'{nome_do_zip}.zip', 'w') as zip:
            for caminho_anexo in caminho_arquivo:
                zip.write(caminho_anexo, os.path.basename(caminho_anexo))