import os

arquivo_csv_path = os.path.abspath('.') + '/arquivos/Relatorio_cadop.csv'
arquivo_sql_path = os.path.abspath('.') + '/importa_dados_csv.sql'
with open(arquivo_sql_path, 'r') as f:
    conteudo_sql = f.read()
    diretorio_anterior = conteudo_sql.split('\'')[1]
    conteudo_substituido = conteudo_sql.replace(diretorio_anterior, arquivo_csv_path)

with open(arquivo_sql_path, 'w') as f:
    f.write(conteudo_substituido)