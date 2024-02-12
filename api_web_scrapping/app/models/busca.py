from typing import List
import os
class Busca:
    def __init__(self) -> None:
        self.arquivo_de_busca= os.path.abspath('.') + '/assets/csv/Relatorio_cadop.csv'

    def define_items(self):
        with open(self.arquivo_de_busca, 'r', encoding='utf8') as arquivo:
            conteudo_arquivo = arquivo.read()
            linhas = conteudo_arquivo.split('\n')
            cabecalho = [] 
            for index_linha, linha in enumerate(linhas):
                linha = linha.replace('\"', '')
                lista_conteudo_linha = linha.split(';')
                if index_linha == 0:
                        cabecalho = lista_conteudo_linha
                        continue
                for index_conteudo, conteudo_linha in  enumerate(lista_conteudo_linha):
                    if isinstance(linhas[index_linha-1], dict):
                        linhas[index_linha-1][cabecalho[index_conteudo].lower()] = conteudo_linha
                        continue
                    dic_conteudo = dict()
                    dic_conteudo[cabecalho[index_conteudo]] = conteudo_linha
                    linhas[index_linha-1] = dic_conteudo
            return linhas
        
    def busca_dados_relevantes(self, palavras_chaves: List[str]):
        dados_csv = self.define_items()
        
        resultados = []
        for indice, dicionario in enumerate(dados_csv):
            contagem = 0
            for palavra_chave in palavras_chaves:
                if isinstance(dicionario, dict):
                    for chave, valor in dicionario.items():
                        if isinstance(valor, str) and palavra_chave.lower() in valor.lower():
                            contagem += 1
                else: 
                    continue
            if contagem != 0:   
                resultados.append([indice, contagem])

        resultados = sorted(resultados, key=lambda x: x[1], reverse=True)
        
        lista_dic_resultado = []
        for resultado in resultados:
            lista_dic_resultado.append(dados_csv[resultado[0]])
            
        return lista_dic_resultado
