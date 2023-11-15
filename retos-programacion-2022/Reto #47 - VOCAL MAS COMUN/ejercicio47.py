def encontrar_vocal(texto):
    vocales = ["a", "e", "i", "o", "u"]
    dict_vocales = {}
    if type(texto) == str:
        for letra in texto:
            if letra in vocales:
                if letra in dict_vocales:
                    dict_vocales[letra] += 1
                else:
                    dict_vocales[letra] = 1

        if len(dict_vocales) == 0:
            return ""
        return f"La vocal que más se repite es la: {max(dict_vocales, key = dict_vocales.get)} y aparece {dict_vocales[max(dict_vocales, key = dict_vocales.get)]} veces"
                


print(encontrar_vocal("mazamorra"))
print(encontrar_vocal("mhg"))


