def contruir_diccionario(texto):
    dict_nuevo = {}
    for letra in texto:
        dict_nuevo[letra] = texto.count(letra)
    return dict_nuevo


def heterograma(texto):

    for value in contruir_diccionario(texto).values():
        if value > 1:
            return "No es un heterograma"
    return "Es un heterograma"


def isograma(texto):
    order = 0
    for value in contruir_diccionario(texto).values():

        if order == 0:
            order = value
        if order != value:
            return "No es un isograma"
    return "Es un isograma"
 

def pangrama(texto):
    if len(contruir_diccionario(texto).keys()) == 27:
        return "Es un pangrama"
    return "No es un pangrama"
    


print(heterograma("hiperblanduzcos"))
print(isograma("anna"))
print(pangrama("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú"))










