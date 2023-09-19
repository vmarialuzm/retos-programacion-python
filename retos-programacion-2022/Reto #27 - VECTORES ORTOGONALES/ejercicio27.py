def vectores_ortogonales(array1: list ,array2: list) -> bool:
    suma = 0

    for num,i in enumerate(array1):
        suma += i*array2[num]
    
    if suma == 0:
        return True
    return False


print(vectores_ortogonales([1, -2], [-2, 4]))
print(vectores_ortogonales([1, -2], [-2, -1]))
