CREATE TABLE `dados_cadastrais_das_operadoras_ativas_ans` {
    `Registro_ANS` INT PRIMARY KEY NOT NULL,
    `CNPJ` VARCHAR(14) NOT NULL,
    `Razao_Social` VARCHAR(150) NOT NULL,
    `Nome_Fantasia` VARCHAR(80) DEFAULT NULL,
    `Modalidade` VARCHAR(40) NOT NULL,
    `Logradouro` VARCHAR(35) NOT NULL,
    `Numero` int NOT NULL,
    `Complemento` VARCHAR(60) DEFAULT NULL,
    `Bairro` VARCHAR(40) NOT NULL
    `Cidade` VARCHAR(35) NOT NULL
    `UF` VARCHAR(2) NOT NULL,
    `CEP` VARCHAR(8) NOT NULL
    `DDD`INT DEFAULT NULL,
    `Telefone` VARCHAR(8) DEFAULT NULL,
    `Fax` VARCHAR(10) DEFAULT NULL
    `Endereco_eletronico` VARCHAR(80) NOT NULL,
    `Representante` VARCHAR(225) NOT NULL,
    `Cargo_Representante` VARCHAR(50) NOT NULL,
    `Regiao_de_Comercializacao` INT DEFAULT NULL,
    `Data_Registro_ANS` DATE NOT NULL
}
