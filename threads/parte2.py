from threading import Thread
import time

def print_com_delay(texto,delay):
    time.sleep(delay)
    print(texto)

t = Thread(target=print_com_delay,args=("Hello world",6))
t.start()

while t.is_alive():
    print("Esperando a Thread terminar...")
    time.sleep(1)