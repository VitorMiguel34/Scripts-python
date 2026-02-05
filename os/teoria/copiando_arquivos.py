# os + shutil -> mover, renomear a apagar arquivos
import os
import shutil
from pathlib import Path

os.system("clear")
ROOT = Path(__file__).parent
pasta_original = os.path.join(ROOT, "textos")
nova_pasta = os.path.join(ROOT, "pasta_copiada")

os.makedirs(nova_pasta,exist_ok=True)

for root,dirs,files in os.walk(pasta_original):
    for dir in dirs:
        print(f"Criando diretorio: {os.path.join(root,nova_pasta,dir)}")
        os.makedirs(os.path.join(root.replace(pasta_original,nova_pasta),dir), exist_ok=True)
    print(root,dirs,files)
    for file in files:
        caminho_original = os.path.join(root,file)
        caminho_destino = os.path.join(root.replace(pasta_original,nova_pasta))
        print("Caminhos: ",end=" ")
        print(caminho_original,caminho_destino)
        shutil.copy(caminho_original,caminho_destino)