from src.afnd import *
from src.minimiza import *
from src.determiniza import *
from src.uteis import *

afd = {}
alfabeto = []
gramatica = []

while True:
    try:
        token = input()
        if not token:
            break
        gerarAfndToken(afd, token, alfabeto)
    except EOFError:
        break

while True:
    try:
        s = input()
        if not s:
            gerarAfndGramatica(afd, gramatica, alfabeto)
            gramatica.clear()
        else:
            gramatica.append(s)
    except EOFError:
        if gramatica:
            gerarAfndGramatica(afd, gramatica, alfabeto)
        break

eliminarEpsilonTransicoes(afd)
determinizar(afd)
eliminarInalcancaveis(afd)
eliminarInuteis(afd)
exibirAutomatoDeterministico(afd, alfabeto)
