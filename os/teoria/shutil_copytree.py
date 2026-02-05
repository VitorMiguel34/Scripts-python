import os
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
pasta_original = ROOT / "textos"
pasta_destino = ROOT / "pasta_copiada2"

shutil.copytree(src=pasta_original,dst=pasta_destino)
