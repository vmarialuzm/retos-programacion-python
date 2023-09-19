def ordenar_lista(numeros: list, option: str) -> list:
    lista_ordenada = []

    for ind_numeros, numero in enumerate(numeros):
        if not lista_ordenada:
            lista_ordenada.append(numero)
        else:
            contador = len(lista_ordenada)
            while contador:
                if numero >= lista_ordenada[contador-1]:
                    lista_ordenada.insert(contador, numero)
                    break

                if contador == 1 and len(lista_ordenada) == ind_numeros:
                    lista_ordenada.insert(contador-1, numero)


                contador -= 1
            
    option = option.lower()

    if option == "asc":
        return lista_ordenada
    elif option == "desc":
        return lista_ordenada[::-1]
    else:
        return "Debe escribir asc o desc"
              


print(ordenar_lista([4, 6, 1, 8, 2], "Asc"))
print(ordenar_lista([2, 4, 6, 8, 9], "desc"))