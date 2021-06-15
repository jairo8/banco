from gerente import funcoesgerente
from gerente.telas import imprimir
from gerente import traduzir

def login():
    while True:
        email = input(traduzir.traduzir("Informe seu email"))
        senha = input(traduzir.traduzir("Informe sua senha: "))
        if funcoesgerente.fazerLogin(email, senha):
            imprimir.imprimir("Logado com êxito!")
            break
        imprimir.imprimir("Email ou senha incorrétos!")