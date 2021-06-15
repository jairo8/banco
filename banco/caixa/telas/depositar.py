from caixa import funcoescaixa
from caixa.telas import imprimir
from caixa import traduzir

def depositar():
    while True:
        conta = input(traduzir.traduzir("Informe o número da conta de destino:"))
        para = int(input(traduzir.traduzir("Dijite 1 para depositar em sua conta 2 para depositar em uma conta diferente")))
        valor = float(input(traduzir.traduzir("Qual valor que deseja depositar:")))
        modo = 0
        if para == 1:
            modo = 1
            senha = input(traduzir.traduzir("Informe sua senha numérica de 6 díjitos"))
        elif para == 2:
            modo = 2
            senha = ""
        else:
            imprimir.imprimir("Opção inválida")
        if modo != 0:
            if funcoescaixa.depositar(conta, valor, senha, modo):
                imprimir.imprimir("Valor depositado com êxito!")
                break
        imprimir.imprimir("Conta ou senha incorrétos")