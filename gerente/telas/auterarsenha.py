from gerente import funcoesgerente
from gerente.telas import imprimir
from gerente import traduzir

def auterar(tipo):
    while True:
        email = input(traduzir.traduzir("Informe o E-mail do {}: ", tipo))
        if tipo == "gerente":
            while True:
                senha = input(traduzir.traduzir("Informe a senha de acesso: "))
                senha2 = input(traduzir.traduzir("Repita a senha digitada anteriormente: "))
                if senha == senha2:
                    break
                imprimir.imprimir("As senhas digitadas não são iguais")
        else:
            senha = ""
        dados = funcoesgerente.auterarSenha(email, tipo, senha) 
        if dados != "":
            if tipo == "cliente":
                imprimir.imprimir(traduzir.traduzir(dados))
                break
            imprimir.imprimir("Senha auterada com sucesso!")
            break
        imprimir.imprimir("Esse E-mail não existe")