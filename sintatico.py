import json
import copy

slr_tab = open("slr.json", 'r')
gram = open("grm_sint.txt", "r")
simb_tab = open("TabelaSimbolos", 'r')

slr_t = slr_tab.read()
grm = gram.readlines()
tabsim = simb_tab.readlines()

slr_tab.close()
gram.close()
simb_tab.close()

fita = []
pilha = []
regras = []
ts = []
acao = ' '

pilha.insert(0, 0)

for simbolos in tabsim:
    simbolo = simbolos.split("!")
    simbolo[2] = simbolo[2][:-1]
    ts.append(simbolo)
    fita.append(simbolo)
fita.append([0,'$','$'])

for regra in grm:
    rgr = []
    nome, prod = regra.split("->")
    rgr.append(nome.strip())
    rgr.append(len(prod.split()))
    if(prod.strip() == "''"):
        rgr[1] = 0
    regras.append(rgr)

slr = json.loads(slr_t)

while(acao != 'acc'):
    acao = slr['table'][pilha[0]][fita[0][1]]
    if(acao == slr['table'][0]['num']):
        print('\nErro de sintaxe: \nLinha ' + fita[0][2] + ': ' + fita[0][0])
        exit()
    if(acao == 'acc'):  # Estado de aceitação
        break
    if(acao[0] == 's'): # Ação de empilhamento
        pilha.insert(0, fita[0])
        pilha.insert(0, int(acao[1:]))
        fita.pop(0)
    else:               # Ação de redução
        rgr = int(acao[1:])
        for r in range(2*regras[rgr][1]):
            pilha.pop(0);
        pilha.insert(0, regras[rgr][0]);
        pilha.insert(0, int(slr['table'][pilha[1]][pilha[0]]));
print("\nCódigo sintaticamente correto")

declaradas = []
v = []
opr = ['/', '*', '-', '+', '=']

for i in range(len(ts)):
    if(ts[i][1] == 'int'):
        variaveis = []
        variaveis.append(ts[i][0])
    if(ts[i][1] == 'var' and 'int' in variaveis):
        if(ts[i - 1][0] not in opr):
            variaveis.append(ts[i][0])
    if(ts[i][1] == 'endline' and 'int' in variaveis):
        variaveis.remove('int')
        if(variaveis):
            for var in variaveis:
                if(var in declaradas):
                    print("\nErro semântico:\n Linha " + ts[i][2] + ": varíavel " + var + " já declarada")
                    exit(0)
                declaradas.append(var)

print("\nNão foi detectada nenhuma variavel duplicada")
