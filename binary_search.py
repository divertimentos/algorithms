from sorted_list import sorted_list
input_list = sorted_list(200)

# 1ª regra de parada: encontramos o número!
# 2ª regra de parada: a lista tiver length == 1 

def print_lista(lista, left, right):
    print(f"Left: {left}")
    print(f"Right: {right}")
    print(lista[left:right], end="\n\n")

def binary_search(lista, target):
    left_boundary = 0
    right_boundary = len(lista) - 1

    while left_boundary != right_boundary: 
        print_lista(lista, left_boundary, right_boundary)
        middle = (left_boundary + right_boundary) // 2 
        middle_value = lista[middle]
        if middle_value == target:
            return True

        if middle == left_boundary:
            return False
        
        if target < middle_value:
            right_boundary = middle
        else:
            left_boundary = middle

print(binary_search(input_list, 32))
