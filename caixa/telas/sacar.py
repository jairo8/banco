from caixa import funcoescaixa
from caixa.telas import imprimir
from caixa import traduzir

def sacar():
    while True:
        valor = float(input(traduzir.traduzir("Informe o valor que deseja sacar")))
        conta = input(traduzir.traduzir("Informe o número da sua conta?"))
        senha = input(traduzir.traduzir("Informe sua senha numérica de 6 díjitos"))
        if funcoescaixa.sacar(conta, valor, senha):
            imprimir.imprimir("valor sacado com êxito!")
            break
        imprimir.imprimir("Conta ou senha incorrétas")