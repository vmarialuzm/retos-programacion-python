def dibujar_figuras(lado, figura):
    
    if figura == "cuadrado":
        [print("* "*lado) for i in range(lado)]
            
        
    elif figura == "triangulo":
        [print((lado-i)*" " + i*"* ") for i in range(lado+1)]
            


dibujar_figuras(5, "cuadrado")
dibujar_figuras(5, "triangulo")