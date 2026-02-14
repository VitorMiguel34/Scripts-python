from threading import Thread, Lock
import time

class Ingressos:
    def __init__(self,estoque:int):
        self.estoque = estoque
        self.lock = Lock()
    
    def comprar(self,quantidade:int):
        self.lock.acquire()
        if self.estoque < quantidade:
            print("Nao temos estoque suficiente")
            self.lock.release()
            return 
        
        time.sleep(1)

        self.estoque -= quantidade
        print(f"Você comprou {quantidade} ingresos, ainda temos {self.estoque} ingressos")
        self.lock.release()

ingressos = Ingressos(15)

for i in range(1,20):
    t = Thread(target=ingressos.comprar,args=(i,))
    t.start()