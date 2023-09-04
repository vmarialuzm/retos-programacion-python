def encontrar_caracter_infiltrado(array1: str, array2: str) -> list:
    
    if len(array1) != len(array2):
        raise Exception ("El tamaño de las cadenas de texto tienen que ser iguales")
    
    resultado = []

    for i,letra in enumerate(array2):
        if letra != array1[i]:
            resultado.append(letra)
    return resultado



array1 = "Me llamo mouredev" # 17 caracteres
array2 = "Me llemo mouredov"

print(encontrar_caracter_infiltrado(array1, array2))
