import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from arquivo import arquivo
from gerente.telas import menu
from gerente import funcoesgerente
from gerente import traduzir

funcoesgerente.iniciar()
menu.menu()
sair = input(traduzir.traduzir("Precione enter"))
