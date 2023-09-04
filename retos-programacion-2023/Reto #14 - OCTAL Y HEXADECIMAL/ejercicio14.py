def transformar_octal(numero_base10):

    numero = numero_base10

    # Octal
    octal = ""

    while numero > 0:

        octal = str(numero % 8) + octal
        numero = numero // 8

    octal = 0 if octal == "" else octal
    print (f"{numero_base10} en octal es {octal}")


    numero = numero_base10

    # Hexa
    hex_values = "0123456789ABCDEF"
    hex = ""

    while numero > 0:

        hex = hex_values[numero % 16] + hex
        numero = numero // 16

    hex = 0 if hex == "" else hex
    print (f"{numero_base10} en octal es {hex}")


transformar_octal(0)
transformar_octal(100)
transformar_octal(1000)