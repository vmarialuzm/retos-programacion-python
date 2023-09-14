def converir_milisegundos(dias, horas, minutos, segundos):
    dia_convertido = dias*24*60*60*1000
    hora_convertido = horas*60*60*1000
    minuto_convertido = minutos*60*1000
    segundo_convertido = segundos*1000

    milisegundos = dia_convertido + hora_convertido + minuto_convertido + segundo_convertido
    return milisegundos

print(converir_milisegundos(2, 2, 2, 2))