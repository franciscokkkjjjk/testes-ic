from typing import Iterable, Union
from zipfile import ZipFile
from tabula import read_pdf
import pandas
import os
import requests

class Arquivo:
    def __init__(self) -> None:
        self.caminho_padrao_arquivo = os.path.abspath('.') + '/arquivos/'
        
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
                
    def ler_pdf(self, nome_pdf: str, paginas: Union[str, int, Iterable[int], None] = None):
        lista_de_tabelas = read_pdf(self.caminho_padrao_arquivo + nome_pdf + '.pdf', pages=paginas)
        return lista_de_tabelas
    
    def converte_csv(self, nome_csv, nome_pdf: str, paginas: Union[str, int, Iterable[int], None] = None):
        lista_de_tabelas = self.ler_pdf(nome_pdf=nome_pdf, paginas=paginas)
        if len(lista_de_tabelas) > 0:
            lista_de_tabelas = pandas.concat(lista_de_tabelas)
        if len(lista_de_tabelas) == 0:
            return None
        lista_de_tabelas.to_csv(os.path.join(self.caminho_padrao_arquivo, nome_csv + '.csv'), index=False)
        return lista_de_tabelas