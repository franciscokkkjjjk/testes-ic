def busca_sig_abreviacao_tabela(abreviacao: str, parametro_de_busca: str, pagina: str):
    quantidade_letras_parametro = len(parametro_de_busca)
    num = pagina.find(parametro_de_busca)
    str_temp = pagina[num]
    i = num
    contagem = 0
    while(pagina[i] != '\n'):
        i += 1
        #interrompe o loop caso o loop estiver fora do parametro de busca mais o espaço e a primeira letra do significado, 
        if(quantidade_letras_parametro+2 < contagem) and (pagina[i].isupper()) and (pagina[i-1] != ' '):
            break
        str_temp = str_temp + pagina[i] 
        contagem += 1
    str_temp = str_temp.split(parametro_de_busca)
    return str_temp[1]