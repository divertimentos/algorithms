from sorted_list import sorted_list
input_list = sorted_list(200)

# 1ª regra de parada: encontramos o número!
# 2ª regra de parada: a lista tiver length == 1 

def binary_search(lista, target):
    left_boundary = 0
    right_boundary = len(lista) - 1
    focal_point = left_boundary + (right_boundary - left_boundary // 2) 
    focal_point == target
    

print(binary_search(input_list, 8))


# [0, 0, 0, 0, 0, 0, 0, 0, 0]
#              |     /     |
#              5           10
