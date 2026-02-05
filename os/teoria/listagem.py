import os
from pathlib import Path

os.system('clear')
caminho = Path(__file__).parent
for item in os.listdir(caminho):
    print(item)
    if os.path.isdir(item):
        caminho_pasta = caminho / item
        print(f"Diretorio {item}:")
        for arquivo in os.listdir(caminho_pasta):
            print(arquivo)