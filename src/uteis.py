def unirEstados(automato, estados):
    # É feita a união de todos os estados do automato que estão na lista estados
    final = {}
    def une(estado):
        for e in estado:
            if e in final:
                final[e] = unirListas(final[e], estado[e])
            else:
                final.update({e: estado[e]})

    for estado in estados:
        une(automato[estado])
    return final


def unirListas(l1, l2):
    return l1 + list(set(l2) - set(l1))


def unirAutomatos(afd, aTemp):
    mpEst = {x: x + len(afd) for x in range(len(aTemp))}
    aux = []
    if '&' in afd[0].keys():     # É criado uma nova regra S' que leva a regra S por epsilon transição
        afd[0]['&'].append(mpEst[0])
    else:
        afd[0].update({'&': [mpEst[0]]})
    for chave in aTemp.keys():
        for ch in aTemp[chave].keys():
            if ch == '#':
                continue
            aux = []
            for i in aTemp[chave][ch]:
                aux.append(mpEst[i])
            aTemp[chave][ch] = aux
    for chave in aTemp.keys():
        afd.update({mpEst[chave] : aTemp[chave]})


def exibirAutomatoDeterministico(afnd, alfabeto):
    #alfabeto.sort()
    print('     {}'.format('-----'*len(alfabeto)))
    print('     |', end='')
    for i in alfabeto:
        print('  {:2}|'.format(i), end='')
    print('\n     {}'.format('-----'*len(alfabeto)))
    for i in afnd.keys():
        if '#' in afnd[i].keys():
            print('#', end='')
        else:
            print(' ', end='')
        print('{:3}:|'.format(i), end='')
        for j in alfabeto:
            if j in afnd[i].keys():
                print(' {:2} |'.format(afnd[i][j][0]), end='')
            else:
                print(' {:2} |'.format('-'), end='')
        print('')
    print('     {}'.format('-----'*len(alfabeto)))

def AFDparaLex(afd, alfabeto):
    saida = open("AFDparaLex", "w")

    saida.write(str(len(afd)) + '\n')

    simbolos = ""

    for simbolo in alfabeto:
        simbolos += simbolo + ' '

    simbolos = simbolos[:-1]
    simbolos += '\n'

    saida.write(simbolos)

    for estado in afd:
        estados = ""
        for chave in alfabeto:
            if chave in afd[estado]:
                estados += str(afd[estado][chave][0]) + ' '
            else:
                estados += str(-1) + ' '
        estados = estados[:-1]
        estados += '\n'
        saida.write(estados)
