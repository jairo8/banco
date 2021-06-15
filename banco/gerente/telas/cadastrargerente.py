from gerente import funcoesgerente
from gerente.telas import imprimir
from gerente import traduzir

def cadastrar():
    while True:
        nome = input(traduzir.traduzir("Informe o nome do gerente"))
        cpf = input(traduzir.traduzir("Informe os 11 dijitos do CPF"))
        email = input(traduzir.traduzir("Informe o email do gerente"))
        telefone = input(traduzir.traduzir("Informe o telefone do gerente"))
        while True:
            senha = input(traduzir.traduzir("Informe a senha de acesso:"))
            senha2 = input(traduzir.traduzir("Repita a senha dijitada anteriormente: "))
            if senha == senha2:
                break
            imprimir.imprimir("As senhas dijitadas não são iguais")
        dados = funcoesgerente.cadastrarGerente(nome, cpf, email, telefone, senha)
        if dados == 0:
            imprimir.imprimir("O nome é obrigatório!")
        elif dados == 1:
            imprimir.imprimir("O CPF é obrigatório ou está inválido")
        elif dados == 2:
            imprimir.imprimir("O e-mail é obrigatório ou já existe no sistema")
        elif dados == 3:
            imprimir.imprimir("Telefone inválido ou embranco")
        elif dados == 4:
            imprimir.imprimir("Senha embranca ou inválida")
        else:
            imprimir.imprimir("Gerente cadastrado com sucesso!")
            break
        imprimir.imprimir("Erro ao cadastrar gerente")