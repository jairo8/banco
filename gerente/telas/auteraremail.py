from gerente import funcoesgerente
from gerente.telas import imprimir
from gerente import traduzir

def auterar(tipo):
    while True:
        email = input(traduzir.traduzir("Informe o E-mail do {}: ", tipo))
        email2 = input(traduzir.traduzir("Informe o novo e-mail de acesso: "))
        if funcoesgerente.auterarEmail(email, tipo, email2) != "":
            imprimir.imprimir("E-mail auterado com sucesso!")
            break
        imprimir.imprimir("Esse E-mail não existe")