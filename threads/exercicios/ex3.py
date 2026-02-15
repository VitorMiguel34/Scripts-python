from threading import Thread
from time import sleep
import random
import queue

tarefas = queue.Queue()
for i in range(1,21):
    tarefas.put(f"Tarefa {i}")

def resolver_tarefa():
    while not tarefas.empty():
        tarefa = tarefas.get()
        print(f"Resolvendo {tarefa}")
        sleep(random.randint(1,3))
        print(f"{tarefa} resolvida!")
        tarefas.task_done()

threads = []
for i in range(3):
    t = Thread(target=resolver_tarefa)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
    
