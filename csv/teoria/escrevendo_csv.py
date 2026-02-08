from lendo_csv import ROOT
import csv

nome_arquivo = "escrevendo.csv"
caminho_arquivo = ROOT / nome_arquivo

lista_pessoas = [ 
    {"nome": "Julia", "idade": 17},
    {"nome": "Marcos", "idade": 18}
]

colunas = lista_pessoas[0].keys()

'''
with open(caminho_arquivo,"w") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(colunas)

    for pessoa in lista_pessoas:
        escritor.writerow(pessoa.values())'''

with open(caminho_arquivo,"w") as arquivo:
    escritor = csv.DictWriter(arquivo,fieldnames=colunas)
    escritor.writeheader()

    for pessoa in lista_pessoas:
        escritor.writerow(pessoa)