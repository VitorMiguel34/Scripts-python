import os
import json
from pathlib import Path

ROOT = Path(__file__).parent
nome_arquivo = "main.json"
caminho_arquivo = os.path.join(ROOT,nome_arquivo)

string = '''
{
    "nome": "Victor",
    "idade": 15
}
'''

json_pessoa = json.loads(string)

with open(caminho_arquivo,"w") as arquivo:
    json.dump(json_pessoa,arquivo, ensure_ascii=False, indent=2)

with open(caminho_arquivo,"r") as arquivo:
    print(json.load(arquivo))