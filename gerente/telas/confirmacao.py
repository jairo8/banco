from gerente.telas import imprimir
from gerente import traduzir

def confirmacao(mensagem):
    while True:
        opcao = input(traduzir.traduzir(mensagem))
        if opcao.lower() == "s":
            return True
        elif opcao.lower() == "n":
            return False
        imprimir.imprimir("opção inválida")