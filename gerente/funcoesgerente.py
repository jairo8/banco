import random
from arquivo import arquivo
from gerente import tempo
from gerente.telas import cadastrargerente
from gerente.telas import login
from gerente.telas import idioma
from gerente import traduzir

def fazerLogin(email, senha):
    gerentes = arquivo.ler("../gerente/gerentes.json")
    if arquivo.chaveExiste(gerentes, "email", email):
        for i in gerentes:
            if gerentes[i]["email"] == email:
                if gerentes[i]["senha"] == senha:
                    dicionario = {"email": email, "senha": senha}
                    arquivo.adicionar(dicionario, "../gerente/logado.json")
                    return True
    return False

def cadastrarGerente(nome, cpf, email, telefone, senha):
    codigos = arquivo.ler("../gerente/codigos.json")
    gerentes = arquivo.ler("../gerente/gerentes.json")
    if arquivo.chaveExiste(gerentes, "email", email) or email == "":
        return 2
    if len(cpf) == 11 and cpf != "":
        cpf = validarCPF(cpf)
    else:
        return 1
    if (len(telefone) == 10 or len(telefone) == 11) and telefone != "":
        telefone = validarTelefone(telefone)
    else:
        return 3
    if nome == "":
        return 0
    if validarSenha(senha) == False or senha == "":
        return 4
    dicionario = {"nome": nome, "cpf": cpf, "email": email, "telefone": telefone, "senha": senha}
    codigo = codigos["gerente"]
    gerentes[codigo] = dicionario
    arquivo.adicionar(gerentes, "../gerente/gerentes.json")
    codigo += 1
    codigos["gerente"] = codigo
    arquivo.adicionar(codigos, "../gerente/codigos.json")

def removerGerente(codigo):
    gerentes = arquivo.ler("../gerente/gerentes.json")
    gerentes.pop(codigo)
    arquivo.adicionar(gerentes, "../gerente/gerentes.json")

def cadastrarCliente(nome, cpf, email, telefone, endereco, tipoDeConta):
    clientes = arquivo.ler("../gerente/clientes.json")
    codigos = arquivo.ler("../gerente/codigos.json")
    if arquivo.chaveExiste(clientes, "email", email) or email == "":
        return 2
    if len(cpf) == 11 and cpf != "":
        cpf = validarCPF(cpf)
    else:
        return 1
    if (len(telefone) == 10 or len(telefone) == 11) and telefone != "":
        telefone = validarTelefone(telefone)
    else:
        return 3
    if nome == "":
        return 0
    if endereco == "":
        return 4
    dicionario = {"nome": nome, "cpf": cpf, "email": email, "telefone": telefone, "endereco": endereco}
    numeroConta = str(codigos["conta"])
    dijito = str(random.randint(0, 9))
    numeroConta += "-" + dijito
    senha = str(random.randint(111111, 999999))
    dicionario2 = {"numeroConta": numeroConta, "saldo": 0, "tipo": tipoDeConta, "senha": senha, "hextrato": {}}
    dicionario["conta"] = dicionario2
    codigo = codigos["cliente"]
    clientes[codigo] = dicionario
    codigos["cliente"] += 1
    codigos["conta"] += 1
    arquivo.adicionar(codigos, "../gerente/codigos.json")
    arquivo.adicionar(clientes, "../gerente/clientes.json")
    dados = traduzir.traduzir("numero da conta: {}\nsenha: {}", numeroConta, senha)
    return dados

def removerCliente(codigo):
    clientes = arquivo.ler("../gerente/clientes.json")
    pendentes = arquivo.ler("../gerente/pendentes.json")
    if arquivo.chaveExiste(pendentes, "conta", clientes[codigo]["conta"]["numeroConta"]):
        return False
    clientes.pop(codigo)
    arquivo.adicionar(clientes, "../gerente/clientes.json")
    return True

def recuperarSenha(email, tipo):
    gerentes = arquivo.ler("../gerente/gerentes.json")
    clientes = arquivo.ler("../gerente/clientes.json")
    if tipo == "cliente":
        if arquivo.chaveExiste(clientes, "email", email):
            codigo = arquivo.codigoChave(clientes, "email", email)
            return clientes[codigo]["conta"]["senha"]
        return ""
    elif tipo == "gerente":
        if arquivo.chaveExiste(gerentes, "email", email):
            codigo = arquivo.codigoChave(gerentes, "email", email)
            return gerentes[codigo]["senha"]
        return ""

def auterarSenha(email, tipo, senha = ""):
    gerentes = arquivo.ler("../gerente/gerentes.json")
    clientes = arquivo.ler("../gerente/clientes.json")
    if tipo == "cliente":
        if arquivo.chaveExiste(clientes, "email", email):
            codigo = arquivo.codigoChave(clientes, "email", email)
            senha = str(random.randint(111111, 999999))
            clientes[codigo]["conta"]["senha"] = senha
            arquivo.adicionar(clientes, "../gerente/clientes.json")
            return traduzir.traduzir("novaSenha:{}", senha)
        return ""
    elif tipo == "gerente":
        if arquivo.chaveExiste(gerentes, "email", email):
            codigo = arquivo.codigoChave(gerentes, "email", email)
            gerentes[codigo]["senha"] = senha
            arquivo.adicionar(gerentes, "../gerente/gerentes.json")
            return traduzir.traduzir("novaSenha: {}", senha)
        return ""

def auterarEmail(email, tipo, email2 = ""):
    gerentes = arquivo.ler("../gerente/gerentes.json")
    clientes = arquivo.ler("../gerente/clientes.json")
    if tipo == "cliente":
        if arquivo.chaveExiste(clientes, "email", email) and arquivo.chaveExiste(clientes, "email", email2) == False:
            codigo = arquivo.codigoChave(clientes, "email", email)
            clientes[codigo]["email"] = email2
            arquivo.adicionar(clientes, "../gerente/clientes.json")
            return "E-mail auterado"
        return ""
    elif tipo == "gerente":
        if arquivo.chaveExiste(gerentes, "email", email) and arquivo.chaveExiste(gerentes, "email", email2) == False:
            codigo = arquivo.codigoChave(gerentes, "email", email)
            gerentes[codigo]["email"] = email2
            arquivo.adicionar(gerentes, "../gerente/gerentes.json")
            return "E-mail auterado"
        return ""

def permitir(codigo, codigoDestino):
    contas = arquivo.ler("../gerente/clientes.json")
    pendentes = arquivo.ler("../gerente/pendentes.json")
    contas = adicionarEstrato(contas, traduzir.traduzir("depósito deR${:.2f} recebido", pendentes[codigo]["valor"]), contas[codigoDestino]["conta"]["numeroConta"])
    contas[codigoDestino]["conta"]["saldo"] += pendentes[codigo]["valor"]
    pendentes.pop(codigo)
    arquivo.adicionar(contas, "../gerente/clientes.json")
    arquivo.adicionar(pendentes, "../gerente/pendentes.json")

def adicionarEstrato(dicionario, mensagem, conta):
    codigos = arquivo.ler("../gerente/codigos.json")
    codigo = contaExiste(dicionario, conta)
    codigo2 = codigos["historico"]
    dicionario2 = {"data": "{}, {}".format(traduzir.traduzir(tempo.dia()), tempo.data()), "hora": tempo.hora(), "mensagem": mensagem}
    dicionario[codigo]["conta"]["hextrato"][codigo2] = dicionario2
    codigos["historico"] += 1
    arquivo.adicionar(codigos, "../gerente/codigos.json")
    return dicionario

def contaExiste(dicionario, numero):
    for i in dicionario:
        if dicionario[i]["conta"]["numeroConta"] == numero:
            return i
    return ""

def validarCPF(cpf):
    cpf2 = ""
    for     letra in cpf:
        cpf2 += letra
        if len(cpf2) == 3:
            cpf2 += "."
        if len(cpf2) == 7:
            cpf2 += "."
        if len(cpf2) == 11:
            cpf2 += "-"
    return cpf2

def validarTelefone(telefone):
    telefone2 = ""
    for letra in telefone:
        if len(telefone2) == 0:
            telefone2 += "("
        if len(telefone2) == 3:
            telefone2 += ") "
        if len(telefone) == 10 and len(telefone2) == 9:
            telefone2 += "-"
        if len(telefone) == 11 and len(telefone2) == 10:
            telefone2 += "-"
        telefone2 += letra
    return telefone2

def validarSenha(senha):
    contadorMaiusculo = 0
    contadorMinusculo = 0
    contadorNumero = 0
    for letra in senha:
        if letra.isdigit():
            contadorNumero += 1
        if letra.isupper():
            contadorMaiusculo += 1
        if letra.islower():
            contadorMinusculo += 1
    if contadorMaiusculo >= 1 and contadorMinusculo >= 1 and contadorNumero >= 1 and len(senha) >= 8:
        return True
    return False

def iniciar():
    if arquivo.arquivoExiste("../gerente/codigos.json") == False:
        dicionario = {
            "gerente": 100000,
            "conta": 100000,
            "cliente": 100000,
            "historico": 100000,
            "pendentes": 100000
        }
        arquivo.adicionar(dicionario, "../gerente/codigos.json")
    gerentes = arquivo.ler("../gerente/gerentes.json")
    config = arquivo.ler("../gerente/config.json")
    clientes = arquivo.ler("../gerente/clientes.json")
    if len(config) == 0:
        dicionario = {"idioma": "pt.lang"}
        arquivo.adicionar(dicionario, "../gerente/config.json")
        idioma.idioma()
    if len(gerentes) == 0:
        cadastrargerente.cadastrar()
        login.login()
    else:
        login.login()
    if len(clientes) == 0:
        dicionario = {}
        arquivo.adicionar(dicionario, "../gerente/pendentes.json")

def alterarIdioma(nome):
    config = arquivo.ler("../gerente/config.json")
    config["idioma"] = nome
    arquivo.adicionar(config, "../gerente/config.json")