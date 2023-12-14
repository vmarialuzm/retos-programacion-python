def calcular_puntos_palabra():
    dict_equivalencias = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'ñ': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19,
        's': 20, 't': 21, 'u': 22, 'v': 23, 'w': 24, 'x': 25, 'y': 26, 'z': 27
    }
    puntos = 0

    while puntos != 100:
        
        palabra = input("Introduce una palabra: ").lower()

        for letra in palabra:
            punto = dict_equivalencias[letra]
            puntos += punto
        
        print(f"La palabra {palabra} tiene {puntos} puntos")


calcular_puntos_palabra()

