from .uteis import *

def eliminarEpsilonTransicoes(afnd):
    epsilon = []
    for chave in afnd.keys():
        if '&' in afnd[chave]:
            epsilon.append(chave)
    def copiarRegras(regras, nRegra):      # Recursivamente copia regras que são acessadas por uma epsilon transição
        if nRegra not in epsilon:
            return    #Caso não tenha epsilon transições na regra
        epsilon.remove(nRegra)
        for regra in regras['&']:
            chaves = afnd[regra].keys()
            if '&' in chaves:
                copiarRegras(afnd[regra], regra)
                regras['&'] = unirListas(regras['&'], afnd[regra]['&'])
        afnd[nRegra] = unirEstados(afnd, regras['&'] + [nRegra])

    epAux = epsilon.copy()
    for ep in epAux:
        copiarRegras(afnd[ep], ep)
    for ep in epAux:
        del afnd[ep]['&']


def determinizar(afnd):
    mpRgs = {}
    visitados = set()
    def determiniza(regra, nReg):       # Recursivamente determiniza o automato
        if nReg in visitados:
            return
        visitados.add(nReg)
        chaves = list(regra.keys())
        for chave in chaves:
            if len(regra[chave]) > 1:
                regra[chave].sort()
                nRg = str(regra[chave]) # É gerada uma nova regra que será mapeada no mpReg
                if nRg not in mpRgs.keys():
                    nEst = len(afnd)    # Novo estado que será mapeado pela variavel nRg
                    mpRgs.update({nRg: nEst})
                    afnd.update({len(afnd): unirEstados(afnd, regra[chave])})
                    determiniza(afnd[nEst], nEst)
                regra.update({chave: [mpRgs[nRg]]})
    i, t = 0, len(afnd)
    while i < t:
        determiniza(afnd[i], i)
        i, t = i + 1, len(afnd)    # Cada nova regra criada também deve ser determinizada
