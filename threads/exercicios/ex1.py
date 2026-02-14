from threading import Thread
from time import sleep
import string

alfabeto = string.ascii_lowercase

def mostrar_numeros(a,b):
    for i in range(a,b):
        print(i)
        sleep(1)

def mostrar_letras():
    for c in alfabeto:
        print(c)
        sleep(1)

t1 = Thread(target=mostrar_numeros, args=(1,6))
t2 = Thread(target=mostrar_letras)
t1.start()
t2.start()