def reverse(cadena: str) -> str:
    cadena_reverse = ""
    for letra in range(len(cadena)-1,-1,-1):
        cadena_reverse += cadena[letra]
    print(cadena_reverse)

reverse("Hola mundo")



