def reconocer_numero_armstrong(num: int) -> bool:
    num = str(num)
    suma_digitos_potencia = 0

    for i in range(len(num)):
        suma_digitos_potencia += int(num[i])**len(num)
    
    if suma_digitos_potencia == int(num):
        return True
    return False

print(reconocer_numero_armstrong(370))