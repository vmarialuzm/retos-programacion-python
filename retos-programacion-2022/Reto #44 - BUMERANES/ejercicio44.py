def encontrar_bumeranes(numeros):
    n_bumeranes = 0
    if len(numeros)>3:
        for i, numero in enumerate(numeros):

            if numero == numeros[i+2] and numero != numeros[i+1]:
                n_bumeranes += 1
                print([numero, numeros[i+1], numeros[i+2]])
        
            if i == len(numeros)-3:
                break
    else:
        print("Debe ingresar una lista con más de 3 elementos")
    
encontrar_bumeranes([2, 1, 2, 3, 3, 4, 2, 4])
encontrar_bumeranes([2, 1, 2, 1, 2])
encontrar_bumeranes([1, 2, 3, 4, 5])
encontrar_bumeranes([2, 2, 2, 2, 2])
encontrar_bumeranes([2, -2, 2, -2, 2])
encontrar_bumeranes([2, -2])
encontrar_bumeranes([2])
encontrar_bumeranes([])


