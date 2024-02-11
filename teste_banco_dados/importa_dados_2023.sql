use `dados_cadastrais`;

LOAD DATA LOCAL INFILE '-1'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@coluna1,@coluna2,@coluna3,@coluna4,@var_col_inicial, @var_col_final)
SET 
    DATA = @coluna1,
    REG_ANS = @coluna2,
    CD_CONTA_CONTABIL = @coluna3,
    DESCRICAO = @coluna4,
    VL_SALDO_INICIAL = REPLACE(REPLACE(@var_col_inicial, '.', ''), ',', '.'),
    VL_SALDO_FINAL = REPLACE(REPLACE(@var_col_final, '.', ''), ',', '.');

LOAD DATA LOCAL INFILE '-2'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@coluna1,@coluna2,@coluna3,@coluna4,@var_col_inicial, @var_col_final)
SET 
    DATA = @coluna1,
    REG_ANS = @coluna2,
    CD_CONTA_CONTABIL = @coluna3,
    DESCRICAO = @coluna4,
    VL_SALDO_INICIAL = REPLACE(REPLACE(@var_col_inicial, '.', ''), ',', '.'),
    VL_SALDO_FINAL = REPLACE(REPLACE(@var_col_final, '.', ''), ',', '.');

LOAD DATA LOCAL INFILE '-3'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@coluna1,@coluna2,@coluna3,@coluna4,@var_col_inicial, @var_col_final)
SET 
    DATA = @coluna1,
    REG_ANS = @coluna2,
    CD_CONTA_CONTABIL = @coluna3,
    DESCRICAO = @coluna4,
    VL_SALDO_INICIAL = REPLACE(REPLACE(@var_col_inicial, '.', ''), ',', '.'),
    VL_SALDO_FINAL = REPLACE(REPLACE(@var_col_final, '.', ''), ',', '.');