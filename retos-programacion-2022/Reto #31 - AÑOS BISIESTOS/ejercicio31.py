def listar_bisiestos(year):

    lista_bisiestos = []

    while True:
        
        contador = len(lista_bisiestos)
        year += 1

        if str(year).endswith('00'): 
            if year % 400 == 0:
                lista_bisiestos.append(year)
        elif year % 4 == 0:
              lista_bisiestos.append(year)
        elif contador == 30:
            break
    return lista_bisiestos

print(listar_bisiestos(1795))