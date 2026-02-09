import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import string
import datetime

load_dotenv()

senha = os.getenv("senha")
email = os.getenv("email")
email_destinatario = os.getenv("email_destinatario")
host = os.getenv("host")
porta = os.getenv("porta")

assunto_email = "Email teste"

msg = MIMEMultipart()
msg["from"] = email
msg["to"] = email
msg["subject"] = assunto_email

ROOT = Path(__file__).parent
nome_arquivo = "email.txt"
caminho_arquivo = os.path.join(ROOT,nome_arquivo)
dados = dict(
    nome="Victor",
    data=datetime.datetime.strftime(datetime.date.today(),"%d/%m/%Y"),
    remetente="Victor"
)
with open(caminho_arquivo,"r") as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    msg.attach(MIMEText(template.substitute(dados)))

with smtplib.SMTP(host,porta) as server:
    server.ehlo()
    server.starttls()
    server.login(email,senha)
    server.send_message(msg)
    print("Mensagem enviada com sucesso!")