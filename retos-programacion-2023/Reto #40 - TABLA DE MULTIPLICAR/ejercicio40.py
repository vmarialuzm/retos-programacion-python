def tabla_multiplicar(numero):

    try:
        numero = int(numero)
        for i in range(1,11):
            print(f"{numero} x {i} = {i*numero}")

    except Exception as e:
        print({"Error": str(e)})

tabla_multiplicar(5)





