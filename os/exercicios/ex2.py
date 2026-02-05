'''
Cliente diz:

“Quero um backup da minha pasta de trabalho todo dia.”

Requisitos

-Dada uma pasta trabalho/
-Crie uma pasta backup/
-Copie tudo de trabalho/ para backup/
-Se o backup já existir, apague antes e recrie

Regras

Use shutil.copytree
Use shutil.rmtree
Use os.path.exists
'''

import os
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
pasta_original = "ex2_trabalho"
pasta_backup = "ex2_backup"
caminho_original = os.path.join(ROOT,pasta_original)
caminho_backup = os.path.join(ROOT,pasta_backup)
os.makedirs(caminho_original, exist_ok=True)
os.makedirs(caminho_backup, exist_ok=True)

if os.path.exists(caminho_backup):
    shutil.rmtree(caminho_backup)
shutil.copytree(caminho_original,caminho_backup)