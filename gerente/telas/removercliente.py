from gerente import funcoesgerente
from arquivo import arquivo
from gerente.telas import listar
from gerente.telas import confirmacao
from gerente.telas import imprimir
from gerente import traduzir

def remover():
    clientes = arquivo.ler("../gerente/clientes.json")
    while True:
        listar.listar(clientes, "nome", True)
        email = input(traduzir.traduzir("Informe o email da conta do cliente a remover"))
        if arquivo.chaveExiste(clientes, "email", email):
            codigo = arquivo.codigoChave(clientes, "email", email)
            senha = input(traduzir.traduzir("informe a senha da conta a remover"))
            if clientes[codigo]["conta"]["saldo"] != 0:
                imprimir.imprimir("Ainda temos saldo em conta não foi possívelremover!")
                break
            if senha == clientes[codigo]["conta"]["senha"]:
                if confirmacao.confirmacao(traduzir.traduzir("Deseja remover o e-mail com a conta {}?", email)):
                    if funcoesgerente.removerCliente(codigo):
                        imprimir.imprimir("Removido exitosamente!")
                        break
                    else:
                        imprimir.imprimir("Não foi possível remover pois há uma ou mais tranzações pendentes para essa conta")
                        break
                else:
                    imprimir.imprimir("Canselado")
            else:
                imprimir.imprimir("Senha incorréta!")
        else:
            imprimir.imprimir("Esse e-mail não existe")