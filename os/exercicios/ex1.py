'''
Leia todos os arquivos da pasta Downloads
Crie pastas automaticamente:
-PDFs
-Imagens
-Videos
-Outros

Mova cada arquivo para sua pasta adequada
'''

import os
import shutil
from pathlib import Path

pastas_por_terminacao = {
    "pdf": "PDFs",
    "mp4": "videos",
    "png": "imagens",
}

ROOT = os.path.join(Path(__file__).parent,"ex1_downloads/")

def criar_pastas(pastas_para_criar: list[str]):
    for pasta in pastas_para_criar:
        caminho = os.path.join(ROOT,pasta)
        os.makedirs(caminho,exist_ok=True)
    os.makedirs(os.path.join(ROOT,"outros"),exist_ok=True)

def apagar_pastas(pastas_para_apagar):
    for pasta in pastas_para_apagar:
        shutil.rmtree(os.path.join(ROOT,pasta))

terminacao_arquivo = lambda arquivo: arquivo.split(".")[-1]

def mover_arquivos(caminho:str):
    for arquivo in os.listdir(caminho):
        if os.path.isfile(os.path.join(caminho,arquivo)):
            terminacao = terminacao_arquivo(arquivo)
            try:
                pasta_destino = pastas_por_terminacao[terminacao]
            except:
                pasta_destino = "outros"

            caminho_destino = os.path.join(caminho,pasta_destino)
            caminho_origem = os.path.join(caminho,arquivo)
            shutil.move(caminho_origem,caminho_destino)

pastas_para_criar = list(pastas_por_terminacao.values())
criar_pastas(pastas_para_criar)
mover_arquivos(ROOT)

