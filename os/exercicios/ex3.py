'''Cliente diz:

“Quero apagar arquivos com mais de 30 dias automaticamente.”

Requisitos

-Percorra uma pasta qualquer
-Verifique a data de modificação dos arquivos
-Apague arquivos com mais de 30 dias'''

import os
from pathlib import Path
from datetime import datetime

pasta = "ex3_pasta"
ROOT = Path(__file__).parent
caminho_pasta = os.path.join(ROOT,pasta)

os.makedirs(caminho_pasta, exist_ok=True)

for arquivo in os.listdir(caminho_pasta):
    caminho_arquivo = os.path.join(caminho_pasta,arquivo)
    if not os.path.isfile(caminho_arquivo):
        continue
    data_modificacao = datetime.fromtimestamp(os.path.getmtime(caminho_arquivo))
    data_atual = datetime.now()
    tempo_modificacao = data_atual - data_modificacao
    dias_modificacao = tempo_modificacao.days
    if dias_modificacao > 30:
        os.remove(caminho_arquivo)

