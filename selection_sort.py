from generate_list import generate_random_list
from time import sleep

lista = generate_random_list(10)

for slow in range(len(lista)):
    print("---" * 6)
    print(f"Ordering position: {slow}")
    for fast in range(slow, len(lista)):
        if lista[fast] < lista[slow]:
            aux = lista[fast]
            lista[fast] = lista[slow]
            lista[slow] = aux
        #  print(f"Verify slow: {lista[slow]}, fast: {lista[fast]}")
        print(lista)
    print(f"Found: {lista[slow]}")
