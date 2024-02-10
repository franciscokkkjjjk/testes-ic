CREATE DATABASE IF NOT EXISTS `dados_cadastrais` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `dados_cadastrais`;

CREATE TABLE `dados_cadastrais_das_operadoras_ativas_ans`(
    `Registro_ANS` integer NOT NULL,
    `CNPJ` VARCHAR(20) NOT NULL,
    `Razao_Social` VARCHAR(150) NOT NULL,
    `Nome_Fantasia` VARCHAR(80) NULL,
    `Modalidade` VARCHAR(40) NOT NULL,
    `Logradouro` VARCHAR(50) NOT NULL,
    `Numero` VARCHAR(30) NOT NULL,
    `Complemento` VARCHAR(60) NULL,
    `Bairro` VARCHAR(40) NOT NULL,
    `Cidade` VARCHAR(35) NOT NULL,
    `UF` VARCHAR(20) NOT NULL,
    `CEP` VARCHAR(10) NOT NULL,
    `DDD`VARCHAR(5) NULL,
    `Telefone` VARCHAR(25) NULL,
    `Fax` VARCHAR(25) NULL,
    `Endereco_eletronico` VARCHAR(80) NULL,
    `Representante` VARCHAR(147) NOT NULL,
    `Cargo_Representante` VARCHAR(50) NOT NULL,
    `Regiao_de_Comercializacao` VARCHAR(20) NULL,
    `Data_Registro_ANS` DATE NOT NULL,
    PRIMARY KEY (`Registro_ANS`)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;


