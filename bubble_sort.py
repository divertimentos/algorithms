from random import randint

lista = []

for i in range(1, 51):
    lista.append(randint(1, 200))

print(f"Lista original: {lista}")

for x in range(len(lista)):
    for y in range(len(lista) - x - 1):
        curr_item = lista[y]
        next_item = lista[y+1] 
        if curr_item > next_item:
            lista[y] = next_item
            lista[y+1] = curr_item

print(f"Lista Ordenada: {lista}")
