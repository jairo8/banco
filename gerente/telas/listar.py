def listar(dicionario, chave, numerada):
    contador = 0
    for l in dicionario:
        if numerada:
            print("{} - {}".format(contador, dicionario[l][chave]))
        else:
            print(dicionario[l][chave])
        contador += 1