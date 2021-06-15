from arquivo import arquivo
from gerente.telas import listararquivos
from caixa import funcoescaixa

def idioma():
    arquivos = arquivo.pegarArquivos("../lang")
    listararquivos.listar(arquivos, True)
    while True:
        numero = int(input("Qual o número correspondente ao idioma escolhido:"))
        if numero >= len(arquivos) or numero < 0:
            print("número inválido")
            continue
        funcoescaixa.alterarIdioma(arquivos[numero])
        break