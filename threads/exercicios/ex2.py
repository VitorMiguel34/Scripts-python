from threading import Thread,Semaphore
from time import sleep
import random

contador = 0
semaforo = Semaphore(3) #Só três pedidos podem ser processados ao mesmo tempo

class Pedido(Thread):
    def __init__(self, numero:int):
        self.numero = numero
        super().__init__()

    def run(self):
        with semaforo:
            print(f"Pedido {self.numero} sendo processado")
            sleep(random.randint(1,3))
            print(f"Pedido {self.numero} finalizado")

for i in range(1,6):
    p = Pedido(i)
    p.start()