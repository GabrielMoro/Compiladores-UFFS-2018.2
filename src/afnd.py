from re import findall as find, match, split
from .uteis import *

def gerarAfndToken(afnd, token, alfabeto):
    if not afnd:
        afnd.update({len(afnd): {}})
    tkInicial = True
    for tk in token:
        if tk not in alfabeto:
            alfabeto.append(tk)
        if tkInicial:   # Token inicial vai para o primeiro estado do automato
            mp = afnd[0]
            if tk in mp.keys():
                mp[tk].append(len(afnd))
            else:
                mp.update({tk : [len(afnd)]})
            tkInicial = False
        else:
            afnd.update({len(afnd) : {tk: [len(afnd) + 1]}})
    afnd.update({len(afnd) : {'#': [1]}})

def gerarAfndGramatica(afnd, gramatica, alfabeto):
    if not afnd:
        afnd.update({0: {}})
    aTemp = {}
    mpRgs = {}
    for regra in gramatica:
        simbolos = find(r'(\w*<\w+>|\w+|&)', regra)
        if simbolos[0] in mpRgs.keys():     # Verifica se a regra já foi criada e armazena no mapa de regras
            iRg = mpRgs[simbolos[0]]    # iRg armazena o índice da regra
        else:
            iRg = len(aTemp)
            aTemp.update({iRg : {}})
            mpRgs.update({simbolos[0]: iRg})
        for simbolo in simbolos[1:]:
            term = find(r'^\w+', simbolo)
            nTerm = find(r'<\w+>', simbolo)
            term = '&' if not term else term[0]
            if term not in alfabeto:
                alfabeto.append(term)
            if not nTerm:       # produção sem não terminal, gera uma regra terminal
                rg = aTemp[iRg]
                if term in rg.keys():
                    rg[term].append(len(aTemp))
                else:
                    rg.update({term : [len(aTemp)]})
                aTemp.update({len(aTemp): {'#':[1]}})
            else:
                nTerm = nTerm[0]
                if nTerm in mpRgs.keys():
                    rg = mpRgs[nTerm]
                else:
                    rg = len(aTemp)
                    mpRgs.update({nTerm: rg})
                    aTemp.update({rg: {}})
                mp = aTemp[iRg]
                if term in mp.keys():
                    mp[term].append(rg)
                else:
                    mp.update({term: [rg]})

    unirAutomatos(afnd, aTemp)
