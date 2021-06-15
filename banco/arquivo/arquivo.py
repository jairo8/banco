import json #importando a biblioteca json para trabalhar com conteúdo em formato json
from pathlib import Path
import os

def adicionar(dicionario, nome):
    with open(nome, "w") as arquivo: #comando para abrir arquivo sem precisar fechar
        json.dump(dicionario, arquivo, indent=4) #colocando o dicionário dentro do arquivo, em formato json

def ler(nome):
    if arquivoExiste(nome):
        with open(nome, "r") as arquivo: #abrindo arquivo para leitura
            dados = json.load(arquivo) #lendo o arquivo e retornando um dicionário
            return dados
    arquivo = open(nome, "w")
    arquivo.write("{\n}")
    arquivo.close()
    return ler(nome)

def chaveExiste(dados, chave, comparador):
    if len(dados) == 0:
        return False
    for key in dados:
        if dados[key][chave] == comparador:
            return True
    return False

def arquivoExiste(nome):
    fileName = nome
    fileObj = Path(fileName)
    fileObj.is_file()
    if fileObj.is_file() == False:
        return False
    return True

def codigoChave(dicionario, chave, procura):
    if chaveExiste(dicionario, chave, procura):
        for i in dicionario:
            if dicionario[i][chave] == procura:
                return i
    return -1

def pegarArquivos(pasta):
    lista = []
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            lista.append(arquivo)
    return lista