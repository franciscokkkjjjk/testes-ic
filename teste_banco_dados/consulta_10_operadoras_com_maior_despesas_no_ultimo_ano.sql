SELECT *, (dc.vl_saldo_final - dc.vl_saldo_inicial) AS despesas
FROM dados_cadastrais.demonstracoes_contabeis dc 
INNER JOIN dados_cadastrais.dados_cadastrais_das_operadoras_ativas_ans dcoaa
ON dc.reg_ans = dcoaa.Registro_ANS
WHERE EXTRACT(YEAR FROM dc.`data`) = 2023
AND dc.descricao LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
ORDER BY despesas ASC
LIMIT 10
