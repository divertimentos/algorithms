from generate_list import generate_random_list

def sorted_list(size):
    lista = generate_random_list(size)
    for slow in range(len(lista)):
        for fast in range(slow, len(lista)):
            if lista[fast] < lista[slow]:
                aux = lista[fast]
                lista[fast] = lista[slow]
                lista[slow] = aux
    return lista

