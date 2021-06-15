from caixa import funcoescaixa
from caixa.telas import imprimir
from caixa import traduzir

def transferir():
    while True:
        conta = input(traduzir.traduzir("Informe o número da sua conta: "))
        contaDestino = input(traduzir.traduzir("Informe o número da conta para qual deseja transferir: "))
        valor = float(input(traduzir.traduzir("Informe o valor que deseja transferir: ")))
        senha = input(traduzir.traduzir("Informe sua senha numérica de 6 díjitos: "))
        resultado = funcoescaixa.transferir(conta, contaDestino, valor, senha)
        if resultado == 0:
            imprimir.imprimir("Conta de origem inválida")
        elif resultado == 1:
            imprimir.imprimir("Conta de destino inválida")
        elif resultado == 2:
            imprimir.imprimir("Saldo insuficiente")
            break
        elif resultado == 3:
            imprimir.imprimir("Senha incorréta")
        else:
            imprimir.imprimir("Transferência realizada com êxito!")
            break
