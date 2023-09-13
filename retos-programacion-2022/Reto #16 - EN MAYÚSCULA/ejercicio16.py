def en_mayuscula(word: str) -> str:
    word_capitalize = ""

    for character in word.split():
        
        word_capitalize += character.replace(character[0],character[0].upper()) + " "
 
    print(word_capitalize)


en_mayuscula("hola mundo")