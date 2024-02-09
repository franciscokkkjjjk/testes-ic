from fastapi import APIRouter
from models.arquivo import Arquivo
from funcoes.funcoes_tabela import busca_sig_abreviacao_tabela
import pandas

routerED = APIRouter()

@routerED.get('/extrairTabelas/{nome_arquivo}')
async def extrairDados(nome_arquivo, paginas=None):
    arq = Arquivo()
    lista_de_tabelas = arq.ler_pdf(nome_pdf=nome_arquivo, paginas=paginas)
    
    if len(lista_de_tabelas) > 0:
        lista_de_tabelas = pandas.concat(lista_de_tabelas)
    if len(lista_de_tabelas) == 0:
        return {
            'mensagem': 'Nenhuma tabela foi encontrada.'
        }
        
    pdf_text = arq.ler_pdf_text(nome_pdf=nome_arquivo, num_maximo_paginas=3)
    lista_de_abreviacoes = ['OD', 'AMB']
    for abreviacao in lista_de_abreviacoes:
        siginificado = busca_sig_abreviacao_tabela(
            parametro_de_busca=f'{abreviacao}: Seg.',
            pagina=pdf_text[3]
        )
        lista_de_tabelas = lista_de_tabelas.rename(
            columns={abreviacao: siginificado})
        lista_de_tabelas = lista_de_tabelas.replace(abreviacao, siginificado)
    
    caminho_absoluto_csv = arq.converte_csv(nome_arquivo, lista_de_tabelas)
    arq.compactar(caminho_absoluto_csv, 'Teste_luis_francisco_brum_gomes')
    return {
        "status_anexo": True
    }