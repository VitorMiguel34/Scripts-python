from zipfile import ZipFile
from pathlib import Path
import shutil
import os

def deletar_arquivos_da_pasta(caminho_pasta: str) -> None:
    for file in os.listdir(caminho_pasta):
        os.unlink(os.path.join(caminho_pasta,file))

def criar_arquivos(quantidade: int, raiz: str) -> None:
    for i in range(quantidade):
        nome_arquivo = f"arquivo{i+1}.txt"
        with open(os.path.join(raiz,nome_arquivo),"w") as arquivo:
            arquivo.write(nome_arquivo)

def main():
    os.system("clear")

    ROOT = Path(__file__).parent
    caminho_pasta = ROOT / "arquivos"
    caminho_zip = ROOT / "pasta_zip" / "arquivo.zip"
    caminho_desempacotado = ROOT / "arquivos_desempacotados"

    caminho_pasta.mkdir(exist_ok=True)
    caminho_desempacotado.mkdir(exist_ok=True)
    criar_arquivos(10,str(caminho_pasta))

    #Criando o zip
    with ZipFile(caminho_zip,"w") as zip:
        for root,dirs,files in os.walk(str(caminho_pasta)):
            for file in files:
                zip.write(os.path.join(root,file),file)

    #Acessando os arquivos do zip
    with ZipFile(caminho_zip,"r") as zip:
        for file in zip.namelist():
            print(file)
    
    #Desempacotando o zip
    with ZipFile(caminho_zip,"r") as zip:
        zip.extractall(caminho_desempacotado)

if __name__ == "__main__":
    main()