import json

slr_tab = open("slr.json", 'r')
gram = open("gramatica_sintatico2.txt", "r")
simb_tab = open("TabelaSimbolos", 'r')

slr = slr_tab.read()
grm = gram.readlines()
tabsim = simb_tab.readlines()

slr_tab.close()
gram.close()
simb_tab.close()
