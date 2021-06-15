import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from caixa.telas import menu
from caixa import funcoescaixa
from caixa import traduzir

funcoescaixa.iniciar()
menu.menu()
sair = input(traduzir.traduzir("Precione enter"))
