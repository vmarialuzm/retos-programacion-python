def conjuntos(array1: set, array2: set, boleano: bool) -> set:
    if boleano:
        return array1.intersection(array2)
    else:
        return array1.symmetric_difference(array2)


print(conjuntos({1, 2, 3, 3, 4}, {2, 2, 3, 3, 3, 4, 6}, True))
print(conjuntos({1, 2, 3, 3, 4}, {2, 2, 3, 3, 3, 4, 6}, False))