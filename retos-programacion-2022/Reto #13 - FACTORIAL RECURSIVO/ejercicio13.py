def recursive_factorial(num: int):
    if num == 1 or num == 0:
        return 1
    else:
        return num * recursive_factorial(num - 1)

#Llamada función principal
if __name__ == '__main__':
    numero = int(input('Introduce un número: '))
    print(f'El factorial de {numero} es:',recursive_factorial(numero))
