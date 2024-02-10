import os

arquivo_csv_path = {
    'all': [os.path.abspath('./arquivos') + '/Relatorio_cadop.csv'],
    '2022': [
        os.path.abspath('./arquivos/2022') + '/1T2022.csv',
        os.path.abspath('./arquivos/2022') + '/2T2022.csv',
        os.path.abspath('./arquivos/2022') + '/3T2022.csv',
        os.path.abspath('./arquivos/2022') + '/4T2022.csv',
    ],
    '2023': [
        os.path.abspath('./arquivos/2023') + '/1T2023.csv',
        os.path.abspath('./arquivos/2023') + '/2T2023.csv',
        os.path.abspath('./arquivos/2023') + '/3T2023.csv',
    ]
}


arquivo_sql_path = [
    os.path.abspath('.') + '/importa_dados_relatorio_cadop_csv.sql',
    os.path.abspath('.') + '/importa_dados_2022.sql',
    os.path.abspath('.') + '/importa_dados_2023.sql',
]

lista_de_consultas = ['all', '2022', '2023']


for index, arquivos_consulta in enumerate(lista_de_consultas):
    arquivos_path = arquivo_sql_path[index].replace('/', '\\')
    print(arquivos_path)
    with open(arquivos_path, 'r') as f:
                conteudo_sql = f.read()
                conteudo_substituido = conteudo_sql
                for index_mandatorio, path_csv in enumerate(arquivo_csv_path[arquivos_consulta], 1):
                    path_csv = path_csv.replace('/', '\\')
                    conteudo_substituido = conteudo_substituido.replace('-' + str(index_mandatorio), path_csv)
                print(conteudo_substituido)
    with open(arquivos_path, 'w') as f:
        f.write(conteudo_substituido)
