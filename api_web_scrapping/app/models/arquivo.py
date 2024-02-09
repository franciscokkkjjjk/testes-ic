from typing import Iterable, Union, Dict, List, Any
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

    def compactar(self, caminho_arquivo: Union[str, List], nome_do_zip: str) -> None:
        with ZipFile(self.caminho_padrao_arquivo + f'{nome_do_zip}.zip', 'w') as zip:
            if(isinstance(caminho_arquivo, list)):
                for caminho in caminho_arquivo:
                    zip.write(caminho, os.path.basename(caminho))
            else: 
                zip.write(caminho_arquivo, os.path.basename(caminho_arquivo))
                
    def ler_pdf(self, nome_pdf: str, paginas: Union[str, int, Iterable[int], None] = None):
        lista_de_tabelas = read_pdf(self.caminho_padrao_arquivo + nome_pdf + '.pdf', pages=paginas)
        return lista_de_tabelas
    
    def converte_csv(self, nome_csv: str, lista_de_tabelas: Union[List[pandas.DataFrame], Dict[str, Any]]):
        caminho_absoluto_csv = os.path.join(self.caminho_padrao_arquivo, nome_csv + '.csv')
        lista_de_tabelas.to_csv(caminho_absoluto_csv, index=False)
        return caminho_absoluto_csv
