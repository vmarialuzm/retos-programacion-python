def marco_palabras(texto):

    lista_palabras = texto.split()
    lista_len = [len(i) for i in lista_palabras]
    max_asteriscos = max(lista_len)
    print((max_asteriscos + 4) * "*")
    
    for i, elemento in enumerate(lista_len):
        print("* " + lista_palabras[i] + " "*(max_asteriscos-elemento) + " *")

    print((max_asteriscos + 4) * "*")

marco_palabras("¿Qué te parece el reto?")
marco_palabras("¿Qué te     parece el reto?")
marco_palabras("¿Cuántos retos de código de la comunidad has resuelto?")