def convertir_binario(numero: int) -> int:

    binario = ""
    provisional = True
    while provisional:
        if numero >= 2:
            parte_entera = numero // 2
            resto = numero % 2
            binario += str(resto)
            numero = parte_entera
        else:
            binario += str(parte_entera)
            binario = binario[::-1]
            provisional = False
    print(binario)

convertir_binario(725)

