# generate list
from random import randint

def generate_random_list(size):
    lista = []
    for i in range(size):
        lista.append(randint(1, 1000))
    return lista
