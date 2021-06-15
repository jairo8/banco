from gerente import funcoesgerente
from gerente.telas import imprimir
from gerente import traduzir

def cadastrar():
    while True:
        nome = input(traduzir.traduzir("Informe seu nome"))
        cpf = input(traduzir.traduzir("Informe seu cpf"))
        email = input(traduzir.traduzir("Informe seu e-mail"))
        telefone = input(traduzir.traduzir("Informe seu telefone"))
        endereco = input(traduzir.traduzir("Informe seu endereço completo"))
        while True:
            tipoDeConta = input(traduzir.traduzir("Qual o tipo de conta? Dijite p para polpansa e c para corrente"))
            if tipoDeConta.lower() == "p":
                break
            elif tipoDeConta.lower() == "c":
                break
            else:
                imprimir.imprimir("Opção inválida!")
        dados = funcoesgerente.cadastrarCliente(nome, cpf, email, telefone, endereco, tipoDeConta.lower())
        if dados == 0:
            imprimir.imprimir("O nome é obrigatório!")
        elif dados == 1:
            imprimir.imprimir("O CPF é obrigatório ou está inválido")
        elif dados == 2:
            imprimir.imprimir("O e-mail é obrigatório ou já existe no sistema")
        elif dados == 3:
            imprimir.imprimir("Telefone inválido ou embranco")
        elif dados == 4:
            imprimir.imprimir("O indereço é obrigatório!")
        else:
            imprimir.imprimir("Cliente cadastrado com sucesso!")
            imprimir.imprimir(dados)
            break
        imprimir.imprimir("Erro ao cadastrar cliente")