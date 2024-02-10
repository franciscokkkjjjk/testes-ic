use `dados_cadastrais`;
LOAD DATA LOCAL INFILE '-1'
INTO TABLE dados_cadastrais_das_operadoras_ativas_ans
FIELDS TERMINATED BY ';'
ENCLOSED by '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

