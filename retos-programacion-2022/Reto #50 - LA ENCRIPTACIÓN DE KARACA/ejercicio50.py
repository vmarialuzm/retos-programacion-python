def encriptar_karaca(texto, is_encriptado):
    dict_equivalencias = {
        "a" : 0,
        "e" : 1,
        "i" : 2,
        "o" : 3,
        "u" : 4
    }

    texto = texto.lower()

    if is_encriptado:
        palabras = texto.split()
        for palabra in palabras:
            palabra = palabra[:-3]
            palabra_alreves = palabra[::-1]
            palabra_alreves = list(palabra_alreves)

            for i, numero in enumerate(palabra_alreves):
                for key, value in dict_equivalencias.items():
                    if numero == str(value):
                        palabra_alreves[i] = key

        
            print("".join(palabra_alreves), end = ' ')    
        print() 

    else:
        palabras = texto.split()

        for palabra in palabras:
            palabra_alreves = palabra[::-1]
            palabra_alreves = list(palabra_alreves)

            for i, letra in enumerate(palabra_alreves):
                if letra in dict_equivalencias:
                    palabra_alreves[i] = str(dict_equivalencias[letra])

        
            print("".join(palabra_alreves)+"aca", end = ' ')    
        print()        
                    



encriptar_karaca("placa", False)
encriptar_karaca("0c0lpaca", True)

encriptar_karaca("Este es el penúltimo reto de programación del año", False)
encriptar_karaca("1ts1aca s1aca l1aca 3m2tlún1paca 3t1raca 1daca nó2c0m0rg3rpaca l1daca 3ñ0aca", True)

