use `dados_cadastrais`;
LOAD DATA INFILE '/home/francisco/projetos/python/testes-ic/teste_banco_dados/arquivos/Relatorio_cadop.csv'
INTO TABLE dados_cadastrais_das_operadoras_ativas_ans
FIELDS TERMINATED BY ';'
ENCLOSED by '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;