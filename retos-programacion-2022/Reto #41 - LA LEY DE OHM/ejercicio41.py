def calcular_parametro(V = None, I = None, R = None):

    if V == None and I != None and R != None:
        return f"V = {round(I * R, 2)}"
    elif V != None and I == None and R != None:
        return f"I = {round(V / R, 2)}"
    elif V != None and I != None and R == None:
        return f"R = {round(V / I, 2)}"
    else:
        return "Invalid values"
    


print(calcular_parametro())
print(calcular_parametro(V = 5.0))
print(calcular_parametro(V = 5.0, R = 4.0))
print(calcular_parametro(V = 5.0, R = 4.0, I = 3.0))
