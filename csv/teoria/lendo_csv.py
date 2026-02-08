import csv
import os
from pathlib import Path

ROOT = Path(__file__).parent
nome_arquivo = "lendo.csv"
caminho_arquivo = ROOT / nome_arquivo

'''
with open(caminho_arquivo,"r") as arquivo:
    csv_ = csv.reader(arquivo)
    for linha in csv_:
        print(linha)'''

if __name__ == "__main__":
    with open(caminho_arquivo,"r") as arquivo:
        csv_ = csv.DictReader(arquivo)
        
        for linha in csv_:
            print(linha["animal"], linha["idade"])