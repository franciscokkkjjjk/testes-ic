use `dados_cadastrais`;
LOAD DATA LOCAL INFILE '-1'
INTO TABLE dados_cadastrais_das_operadoras_ativas_ans
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

