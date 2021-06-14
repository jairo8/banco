from gerente import funcoesgerente
from arquivo import arquivo
from gerente.telas import listar
from gerente.telas import confirmacao
from gerente.telas import imprimir
from gerente import traduzir

def remover():
    gerentes = arquivo.ler("../gerente/gerentes.json")
    while True:
        listar.listar(gerentes, "nome", True)
        email = input(traduzir.traduzir("Informe o e-mail do gerente a remover"))
        if arquivo.chaveExiste(gerentes, "email", email):
            codigo = arquivo.codigoChave(gerentes, "email", email)
            senha = input(traduzir.traduzir("informe a senha da conta a remover"))
            if senha == gerentes[codigo]["senha"]:
                if confirmacao.confirmacao(traduzir.traduzir("Deseja remover o e-mail com a conta {}?", email)):
                    funcoesgerente.removerGerente(codigo)
                    imprimir.imprimir("Removido exitosamente!")
                    break
                else:
                    imprimir.imprimir("Canselado")
            else:
                imprimir.imprimir("Senha incorréta!")
        else:
            imprimir.imprimir("Esse e-mail não existe")