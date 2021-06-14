from caixa import funcoescaixa
from caixa.telas import imprimir
from caixa import traduzir

def verEstrato():
    while True:
        conta = input(traduzir.traduzir("Informe o número da conta: "))
        senha = input(traduzir.traduzir("Informe sua senha numérica de 6 díjitos: "))
        estratos = funcoescaixa.verEstrato(conta, senha)
        if len(estratos) != 0:
            for i in estratos:
                print(traduzir.traduzir("Em {}, as {}, {}", estratos[i]["data"], estratos[i]["hora"], estratos[i]["mensagem"]))
            break
        imprimir.imprimir("Conta ou senha incorrétas")
