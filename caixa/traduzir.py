from arquivo import arquivo

def traduzir(texto, *valores):
    config = arquivo.ler("../caixa/config.json")
    arquivoIdioma = "../lang/" +config["idioma"]
    arquivo2 = open(arquivoIdioma, "r")
    linhas = arquivo2.readlines()
    arquivo2.close()
    dicionario = {}
    for l in linhas:
        traducao = l.split("=")
        dicionario[traducao[0].replace("\\n", "\n")] = traducao[1].replace("\\n", "\n")
    for t in dicionario:
        if t == texto:
            for p in valores:
                tipo = type(2.0)
                if type(p) == tipo and "{:.2f}" in t:
                    dicionario[t] = dicionario[t].replace("{:.2f}", "{:.2f}".format(p), 1)
                else:
                    dicionario[t] = dicionario[t].replace("{}", str(traduzir(p)), 1)
            return dicionario[t]
    for p in valores:
        tipo = type(2.0)
        if type(p) == tipo and "{:.2f}" in texto:
            texto = texto.replace("{:.2f}", "{:.2f}".format(p), 1)
        else:
            texto = texto.replace("{}", str(p), 1)
        return texto
    return texto
