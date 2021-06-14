from arquivo import arquivo
from gerente import funcoesgerente
from gerente.telas import listar
from gerente.telas import confirmacao
from caixa.funcoescaixa import contaExiste
from gerente.telas import imprimir
from gerente import traduzir

def permitir():
    pendentes = arquivo.ler("../gerente/pendentes.json")
    contas = arquivo.ler("../gerente/clientes.json")
    while True:
        if len(pendentes) == 0:
            imprimir.imprimir("Nem um depósito pendente")
            break
        listar.listar(pendentes, "conta", True)
        numero = int(input(traduzir.traduzir("Informe o número correspondente a conta que queres permitir o depósito: ")))
        contador = 0
        codigo = -1
        for c in pendentes:
            if contador == numero:
                codigo = c
                break
            contador += 1
        if codigo == -1:
            imprimir.imprimir("Número incorréto")
            continue
        codigoDestino = contaExiste(contas, pendentes[codigo]["conta"])
        funcoesgerente.permitir(codigo, codigoDestino)
        imprimir.imprimir("Depósito permitido com êxito!")
        break