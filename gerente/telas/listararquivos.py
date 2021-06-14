def listar(arquivos, numerada=False):
    contador = 0
    for a in arquivos:
        if numerada:
            print("{} - {}".format(contador, a.split(".")[0]))
        else:
            print(a.split(".")[0])
        contador += 1