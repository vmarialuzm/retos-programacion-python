def remove_characters(str1 , str2):
    out1 = str1.lower()
    out2 = str2.lower()

    letras_repetidas = []

    for i in out1:
        if i in out2 and i != " ":
            letras_repetidas.append(i)
    
    for letra in letras_repetidas:
        out1 = out1.replace(letra, "")
        out2 = out2.replace(letra, "")

    print(out1)
    print(out2)
            

remove_characters("brais","moure")
remove_characters("Me gusta Java","Me gusta Kotlin")
