from caixa import funcoescaixa
from caixa.telas import imprimir
from caixa import traduzir

def checarSaldo():
    while True:
        conta = input(traduzir.traduzir("Informe o número da conta"))
        senha = input(traduzir.traduzir("Informe sua senha numérica de 6 díjitos"))
        saldo = funcoescaixa.checarSaldo(conta, senha)
        if saldo != -1:
            imprimir.imprimir(traduzir.traduzir("Saldo total em conta: {}", (saldo)))
            break
        imprimir.imprimir("Conta ou senha incorrétas")
