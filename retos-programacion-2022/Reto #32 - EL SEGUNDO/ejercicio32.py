def encontrar_segundo_max(lista_numeros):
    lista_provisional = lista_numeros
    lista_mayores = []

    while len(lista_mayores) < 2:
        num_max = 0
        for i in lista_provisional:
            if i > num_max:
                num_max = i
            else:
                num_max = num_max

        lista_provisional.remove(num_max)
        lista_mayores.append(num_max)

    print(f"El segundo número más grande de la lista es {lista_mayores[-1]}")

encontrar_segundo_max([4, 6, 1, 8, 2])