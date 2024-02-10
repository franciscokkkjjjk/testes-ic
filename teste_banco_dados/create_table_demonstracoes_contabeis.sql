CREATE TABLE `dados_cadastrais`.`demonstracoes_contabeis` (
	`data` DATE NOT NULL,
	`reg_ans` integer NOT NULL,
	`cd_conta_contabil` INT NOT NULL,
	`descricao` VARCHAR(180) NOT NULL,
	`vl_saldo_inicial` VARCHAR(25) NULL,
	`vl_saldo_final` VARCHAR(25) NULL,
    FOREIGN KEY (reg_ans) REFERENCES dados_cadastrais_das_operadoras_ativas_ans(Registro_ANS)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
