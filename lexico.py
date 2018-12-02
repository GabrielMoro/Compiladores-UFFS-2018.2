# from beautifultable import BeautifulTable

AFD = open('AFDparaLex', 'r')
AFDparaLex = AFD.readlines()
cdg = open('codigo.txt', 'r')
codigo = []
codigo = cdg.readlines()
sep = [' ', '=', '>', '<', '+', '-', ',', '*', '**', '/', '(', ')', ';', '\n']
afd = {}
tags = {
36 : 'int',
13 : 'var',
9 : 'equal',
14 : 'num',
10 : 'endline',
33: 'for',
20: 'endfor',
57: 'while',
25: 'endwhile',
37: 'if',
52: 'then',
30: 'else',
27: 'endif',
48: 'show',
44: 'read',
1: 'comma',
2: 'slash',
3: 'asterisk',
4: 'minus',
5: 'plus',
40: 'not',
6: 'less',
7: 'more',
8: 'diff',
11: 'openpar',
12: 'closepar',
}

tabSimb = open('TabelaSimbolos', 'w')

qntEstados = int(AFDparaLex[0])
alfabeto = AFDparaLex[1].split()
estadosFinais = AFDparaLex[qntEstados+2].split()

for simbolo in range(len(alfabeto)):
    afd[alfabeto[simbolo]] = []

for estado in range(2, qntEstados+2):
    transicao = AFDparaLex[estado].split()
    for simbolo in range(len(alfabeto)):
        afd[alfabeto[simbolo]].append(transicao[simbolo])

linhaAtual = 1
for linhaCodigo in range(len(codigo)):
    palavras = []
    inicio = 0
    fim = 0
    for caractere in range(len(codigo[linhaCodigo])):
        if codigo[linhaCodigo][caractere] not in alfabeto and codigo[linhaCodigo][caractere] not in sep:
            print("Esse símbolo não faz parte do alfabeto: " + codigo[linhaCodigo][caractere])
            exit()
        if codigo[linhaCodigo][caractere] not in sep:
            fim += 1
        else:
            palavras.append(codigo[linhaCodigo][inicio:fim])
            if (codigo[linhaCodigo][caractere] != ' ' and codigo[linhaCodigo][caractere] != '\n'):
                palavras.append(codigo[linhaCodigo][caractere])
            inicio = fim = fim + 1
    while '' in palavras:
        palavras.remove('')

    for palavra in palavras:
        estadoAtual = 0
        for caractere in range(len(palavra)):
            estadoAtual = int(afd[palavra[caractere]][estadoAtual])
        if estadoAtual == -1:
            print("Esse token nao existe nessa linguagem: " + palavra)
            exit()
        else:
            tabSimb.write(palavra+'!'+tags[estadoAtual]+'!'+str(linhaAtual)+'\n') #str(estadoAtual)
    linhaAtual += 1
