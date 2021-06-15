from gerente import funcoesgerente
from gerente.telas import imprimir
from gerente import traduzir

def recuperar(tipo):
    while True:
        email = input(traduzir.traduzir("Informe o e-mail{}:", tipo))
        if funcoesgerente.recuperarSenha(email, tipo) != "":
            imprimir.imprimir(funcoesgerente.recuperarSenha(email, tipo))
            break
        imprimir.imprimir("Esse e-mail não existe")