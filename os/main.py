import os 
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

os.system("clear")

print("a"*50)
print("a"*50)
print("a"*50)
print("a"*50)
print("a"*50)
print("a"*50)

API_KEY = os.getenv("API_KEY")
print(f'Chave da API: {API_KEY}')

caminho = os.path.join(Path(__file__).parent,"main.py")
print(caminho)
print(f"Caminho{'' if os.path.exists(caminho) else ' nao'} existe")

diretorio,arquivo = os.path.split(caminho)
print(f"Diretorio: {diretorio}")
print(f"Arquivo: {arquivo}")

os.system("echo Programa finalizado!")

arquivo = "main.py"
nome_arquivo, extensao_arquivo = os.path.splitext(caminho)
print(f"Nome do arquivo: {nome_arquivo}")
print(f"Extensāo do arquivo: {extensao_arquivo}")

print(os.path.abspath("."))
print(os.path.basename(caminho))
print(os.path.dirname(caminho))