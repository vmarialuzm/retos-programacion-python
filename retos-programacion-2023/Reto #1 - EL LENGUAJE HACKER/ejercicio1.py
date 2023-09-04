caracteres_alfanumericos = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
                            "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
                            "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
                            "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}

def transformar_lenguaje_hacker(texto):
    
    nueva_palabra = []
    for caracter in texto:

        if caracter in caracteres_alfanumericos:
            nueva_palabra.append(caracteres_alfanumericos[caracter])

        else:
            nueva_palabra.append(caracter)

    return ''.join(nueva_palabra)



texto = input("Texto a traducir: ").upper()
print(transformar_lenguaje_hacker(texto))