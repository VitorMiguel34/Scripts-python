import shutil
from pathlib import Path

ROOT = Path(__file__).parent
pasta_original = ROOT / "textos"
pasta_destino = ROOT / "pasta_copiada2"

shutil.copytree(src=pasta_original,dst=pasta_destino)

#shutil.rmtree(nova_pasta) apagaria a nova pasta, de forma recursiva