def convertir_temperatura(unidad, grados):
    try:
        if unidad == "°C":
            fahrenheit = (grados*9/5) + 32
            return f"{grados}°C son: {fahrenheit}°F" 
        
        if unidad == "°F":
            celsius = (grados-32)*5/9
            return f"{grados}°F son: {celsius}°C" 
        
        return 'Invalid values'
    
    except TypeError:
            return 'Invalid values'
    
print(convertir_temperatura("°C", 1))
print(convertir_temperatura("C", 1))
print(convertir_temperatura("°F", 33.8))



