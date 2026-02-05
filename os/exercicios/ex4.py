'''
Cliente diz:

“Tenho 300 arquivos com nomes bagunçados. Quero padronizar.”

Requisitos

-Percorrer os arquivos
-Manter a extensão
-Renomear usando os.rename
'''

import os
from pathlib import Path

ROOT = Path(__file__).parent
pasta = "ex4_pasta"
caminho_pasta = os.path.join(ROOT,pasta)

os.makedirs(caminho_pasta, exist_ok=True)

contador = 0
terminacao_arquivo = lambda arquivo: arquivo.split(".")[-1]

def entregar_arquivo(caminho_pasta: str):
    for arquivo in os.listdir(caminho_pasta):
        yield arquivo

qtd_zeros = len(str(len((os.listdir(caminho_pasta))))) - 1

for arquivo in entregar_arquivo(caminho_pasta):
    contador += 1
    caminho_arquivo = os.path.join(caminho_pasta,arquivo)
    if not os.path.isfile(caminho_arquivo):
        continue
    terminacao = terminacao_arquivo(arquivo)
    novo_nome_arquivo = f'Cliente_{"0" * (qtd_zeros - (len(str(contador)) - 1))}{contador}.{terminacao}'
    os.rename(caminho_arquivo,caminho_arquivo.replace(arquivo,novo_nome_arquivo))
    
