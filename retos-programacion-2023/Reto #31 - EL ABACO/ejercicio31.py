def leer_abaco(abaco: list) -> str:

    if len(abaco) != 7:
        raise Exception("Tamaño total incorrecto")

    numero = ""

    for elemento in abaco:
        if len(elemento) == 12 and "---" in elemento and elemento.replace("---", "") == "OOOOOOOOO":
            indice = elemento.index("-")
            numero += str(indice)
        else:
            raise Exception("Formato de fila incorrecto")

    return "{:,}".format(int(numero)).replace(",", ".")
    

abaco = ["O---OOOOOOOO",
         "OOO---OOOOOO",
         "---OOOOOOOOO",
         "OO---OOOOOOO",
         "OOOOOOO---OO",
         "OOOOOOOOO---",
         "---OOOOOOOOO"]

# abaco = ["---OOOOOOOOO",
#          "---OOOOOOOOO",
#          "---OOOOOOOOO",
#          "O---OOOOOOOO",
#          "---OOOOOOOOO",
#          "---OOOOOOOOO",
#          "---OOOOOOOOO"]


print(leer_abaco(abaco))





