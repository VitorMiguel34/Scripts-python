import random
import os

os.system("clear")

r_range = random.randrange(10,20,2)
print(r_range)

inteiro_aleatorio = random.randint(10,20)
print(inteiro_aleatorio)

numero_aleatorio = random.uniform(10,20)
print(numero_aleatorio)

animais = ["cachorro","gato","arara"]
novos_animais = random.sample(animais,k=len(animais))
random.shuffle(animais)
print(animais)
print(novos_animais)

animal_aleatorio = random.choice(animais)
animais_aleatorios = random.choices(animais, k=2)
print(animal_aleatorio)
print(animais_aleatorios)