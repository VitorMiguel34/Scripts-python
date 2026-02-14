from threading import Thread
import time

class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()
    
    def run(self):
        time.sleep(self.tempo)
        print(self.texto)

t1 = MeuThread("thread 1",3)
t1.start()

t2 = MeuThread("thread 2",2)
t2.start()

t3 = MeuThread("thread 3",1)
t3.start()