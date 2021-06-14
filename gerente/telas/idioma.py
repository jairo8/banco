from arquivo import arquivo
from gerente.telas import listararquivos
from gerente import funcoesgerente
from gerente.telas import imprimir
from gerente import traduzir

def idioma():
    arquivos = arquivo.pegarArquivos("../lang")
    listararquivos.listar(arquivos, True)
    while True:
        numero = int(input(traduzir.traduzir("Qual o número correspondente ao idioma escolhido:")))
        if numero >= len(arquivos) or numero < 0:
            imprimir.imprimir("número inválido")
            continue
        funcoesgerente.alterarIdioma(arquivos[numero])
        break