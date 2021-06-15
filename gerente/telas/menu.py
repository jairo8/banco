from gerente import funcoesgerente
from gerente.telas import login
from gerente.telas import cadastrargerente
from gerente.telas import removergerente
from gerente.telas import cadastrarcliente
from gerente.telas import removercliente
from gerente.telas import recuperarsenha
from gerente.telas import auterarsenha
from gerente.telas import auteraremail
from gerente.telas import permitirdeposito
from gerente import traduzir
from gerente.telas import idioma
from gerente.telas import imprimir


def menu():
    while True:
        menu = input(traduzir.traduzir("Tecle sua opção: \ncg- Cadastrar um gerente\nrg- Remover um gerente\ncc- Cadastrar um cliente\nrc- Remover um cliente\nrsc- Recuperação de senha do cliente\nasc- Auterar senha do cliente\nrsg- Recuperação de senha do gerente\n asg- Auterar senha do gerente\naec- Alterar e-mail do cliente\naeg- Alterar e-mail do gerente\npd- Permitir um depósito\nl Alterar idioma do programa\ns- Sair do sistema:")).lower()
        # if menu == 1:
            # login.login()  
        if menu == "cg":
            cadastrargerente.cadastrar()
        if menu == "rg":
            removergerente.remover()
        if menu == "cc":
            cadastrarcliente.cadastrar()
        if menu == "rc":
            removercliente.remover()
        if menu == "rsc":
            recuperarsenha.recuperar("cliente")
        if menu =="asc":
            auterarsenha.auterar("cliente")
        if menu == "rsg":
            recuperarsenha.recuperar("gerente")
        if menu == "asg":
            auterarsenha.auterar("gerente")
        if menu == "aec":
            auteraremail.auterar("cliente")
        if menu == "aeg":
            auteraremail.auterar("gerente")
        if menu == "pd":
            permitirdeposito.permitir()
        if menu == "l":
            idioma.idioma()
        if menu == "s":
            imprimir.imprimir(  "Fim do programa!")
            break
