from beautifultable import BeautifulTable

AFD = open('AFDparaLex', 'r')
AFDparaLex = AFD.readlines()
cdg = open('codigo.txt', 'r')
codigo = []
codigo = cdg.readlines()
sep = [' ', '=', '>', '<', '+', '-', ',', '*', '**', '\'', '/', '\n']
afd = {}

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
            print("kkkkkk troxa esse caractere nao existe/nao faz parte do alfabeto: " + codigo[linhaCodigo][caractere])
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
            print("Esse token nao existe nessa linguagem, seu ignobil " + palavra)
            exit()
        else:
            tabSimb.write(palavra+'!'+str(estadoAtual)+'!'+str(linhaAtual)+'\n')
    linhaAtual += 1
