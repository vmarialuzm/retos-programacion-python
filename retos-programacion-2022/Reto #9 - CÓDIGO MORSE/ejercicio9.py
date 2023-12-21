alfabeto_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}

def transfomar_codigo_morse(frase):
    
    frase = frase.upper()
    frase_convertida = ""
    for letra in frase:
        if letra in alfabeto_morse:
            frase_convertida += alfabeto_morse.get(letra) + " "
        
        elif letra == " " :
            frase_convertida += " "

    print(frase_convertida)


def transformar_lenguaje_natural(frase):
    
    frase = frase.split("  ")
    #print(frase)
    frase_convertida = ""

    dict_inverso = {value:key for key, value in alfabeto_morse.items()}
    #print(dict_inverso)
    for palabra in frase:
        for letra_morse in palabra.split():
            frase_convertida += dict_inverso.get(letra_morse)
        
        frase_convertida += " "
    
    print(frase_convertida.capitalize())


def translate(frase):
    is_morse = False

    for caracter in frase.upper().split():
        if caracter in alfabeto_morse:
            is_morse = True
    
    if is_morse:
        transfomar_codigo_morse(frase)        
    else:
        transformar_lenguaje_natural(frase)
    

translate("hola a todos")
translate(".... --- .-.. .-  .-")