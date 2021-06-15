from arquivo import arquivo
from gerente import tempo
from gerente.funcoesgerente import adicionarEstrato
from caixa.telas import idioma
from caixa import traduzir

def contaExiste(dicionario, numero):
    for i in dicionario:
        if dicionario[i]["conta"]["numeroConta"] == numero:
            return i
    return ""

def depositar(conta, valor, senha, modo):
    contas = arquivo.ler("../gerente/clientes.json")
    pendentes = arquivo.ler("../gerente/pendentes.json")
    codigos = arquivo.ler("../gerente/codigos.json")
    if contaExiste(contas, conta) != "":
        if modo == 1:
            codigo = contaExiste(contas, conta)
            if contas[codigo]["conta"]["senha"] == senha:
                contas[codigo]["conta"]["saldo"] += valor
                contas = adicionarEstrato(contas, traduzir.traduzir("Depósito de R${:.2f} recebido", valor), contas[codigo]["conta"]["numeroConta"])
                arquivo.adicionar(contas, "../gerente/clientes.json")
                return True
        else:
            dicionario = {"conta": conta, "valor": valor}
            codigo = codigos["pendentes"]
            pendentes[codigo] = dicionario
            codigos["pendentes"] += 1
            arquivo.adicionar(pendentes, "../gerente/pendentes.json")
            arquivo.adicionar(codigos, "../gerente/codigos.json")
            return True
    return False

def sacar(conta, valor, senha):
    contas = arquivo.ler("../gerente/clientes.json")
    if contaExiste(contas, conta) != "":
        codigo = contaExiste(contas, conta)
        if contas[codigo]["conta"]["saldo"]-valor >= 0 and contas[codigo]["conta"]["senha"] == senha:
            contas[codigo]["conta"]["saldo"] -= valor
            contas = adicionarEstrato(contas,traduzir.traduzir("saque de r${:.2f} efetuado", valor), conta)
            arquivo.adicionar(contas, "../gerente/clientes.json")
            return True
    return False

def checarSaldo(conta, senha):
    contas = arquivo.ler("../gerente/clientes.json")
    if contaExiste(contas, conta) != "":
        codigo = contaExiste(contas, conta)
        if contas[codigo]["conta"]["senha"] == senha:
            return contas[codigo]["conta"]["saldo"]
    return -1

def transferir(conta, contaDestino, valor, senha):
    contas = arquivo.ler("../gerente/clientes.json")
    if contaExiste(contas, conta) != "":
        codigo = contaExiste(contas, conta)
        if contaExiste(contas, contaDestino) != "" and contaDestino != conta:
            codigoDestino = contaExiste(contas, contaDestino)
            if contas[codigo]["conta"]["saldo"] >= valor:
                if contas[codigo]["conta"]["senha"] == senha:
                    contas[codigo]["conta"]["saldo"] -= valor
                    contas[codigoDestino]["conta"]["saldo"] += valor
                    contas = adicionarEstrato(contas, traduzir.traduzir("Transferência de R${:.2f} realisada para {}", valor, contas[codigoDestino]["nome"]), conta)
                    contas = adicionarEstrato(contas, traduzir.traduzir("Transferência de R${:.2f} recebida de {}", valor, contas[codigo]["nome"]), contaDestino)
                    arquivo.adicionar(contas, "../gerente/clientes.json")
                    return 10
                else:
                    return 3
            else:
                return 2
        else:
            return 1
    else:
        return 0

def verEstrato(conta, senha):
    contas = arquivo.ler("../gerente/clientes.json")
    if contaExiste(contas, conta) != "":
        codigo = contaExiste(contas, conta)
        if contas[codigo]["conta"]["senha"] == senha:
            return contas[codigo]["conta"]["hextrato"]
    return {}

def alterarIdioma(nome):
    config = arquivo.ler("../caixa/config.json")
    config["idioma"] = nome
    arquivo.adicionar(config, "../caixa/config.json")

def iniciar():
    config = arquivo.ler("../caixa/config.json")
    if len(config) == 0:
        dicionario = {"idioma": "pt.lang"}
        arquivo.adicionar(dicionario, "../caixa/config.json")
        idioma.idioma()
