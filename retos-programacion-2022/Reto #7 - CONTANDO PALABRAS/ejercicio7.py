import re

def contador_palabras_repetidas(frase: str) -> int :

    regular_expression = r'[^\w\s]'
    frase = frase.lower()
    lista_palabras_unicas = {}
    
    for palabra in frase.split():
        matches = re.findall(regular_expression, palabra)
        if len(matches) > 0:
            palabra = re.sub(regular_expression, "", palabra)
        
        if palabra in lista_palabras_unicas:
            lista_palabras_unicas[palabra] += 1
        else:
            lista_palabras_unicas[palabra] = 1

    for (key, value) in lista_palabras_unicas.items():
        print(f"{key} se ha repetido {value} vez")
       


contador_palabras_repetidas("Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev).")



