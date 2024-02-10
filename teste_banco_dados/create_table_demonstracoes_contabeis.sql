use `dados_cadastrais`;
CREATE TABLE `demonstracoes_contabeis` (
	`data` DATE NOT NULL,
	`reg_ans` integer NOT NULL,
	`cd_conta_contabil` INT NOT NULL,
	`descricao` VARCHAR(180) NOT NULL,
	`vl_saldo_inicial` FLOAT NOT NULL,
	`vl_saldo_final` FLOAT NOT NULL
) CHARACTER SET utf8mb4 COLLATE UTF8MB4_GENERAL_CI;
