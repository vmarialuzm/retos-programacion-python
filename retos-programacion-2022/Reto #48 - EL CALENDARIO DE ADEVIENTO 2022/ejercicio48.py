from datetime import datetime, timedelta

lista_regalos = [
    'Libros “El programador pragmático”',
    'Videojuegos multiplataforma “while True: learn()”',
    'Cursos "Aprende Javascript ES9, HTML, CSS3 y NodeJS desde cero”',
    'Cursos "Patrones de Diseño en JavaScript y TypeScript”',
    'Pack de libros "Aprende Python en un fin de semana”',
    'Cursos "Desarrollo de Apps iOS con Swift”',
    'Licencias de 6 meses para "Popsy: Crea tu web como un Notion”',
    'Libros "Aprendiendo JavaScript desde cero”',
    'Cursos de "Android con Jetpack Compose desde cero”',
    'Libros "Inteligencia matemática/Apocalipsis matemático"',
    'Cursos "Flutter: Tu guía completa de desarrollo para iOS y Android"',
    'Libros "¿Qué puede salir mal?” de Sandra Ortonobes Lara',
    'Masterclass "Figma para developers”',
    '"Dominios .dev"',
    'Accesos de 3 meses a "Todos los cursos de Mastermind”',
    'Libros "El bosón de Higgs no te va a hacer la cama"',
    'Camisetas "I CODE”',
    'Accesos a "Hack4u", la academia de hacking y ciberseguridad de S4vitar',
    'Libros "Código Sostenible: Cómo desarrollar Software fácil de mantener” de Carlos Blé',
    '"Bootcamps online de programación" (a tu elección) de GeeksHubs Academy',
    'Libros "La artesanía del código limpio" de Robert C. Martin',
    'Accesos a "Todos los cursos de Codely.com"',
    'Libros "Hábitos atómicos: cambios pequeños, resultados extraordinarios" de James Clear',
    'Elige el libro de programación que quieras'
]

def encontrar_regalo(calendario):
    d = datetime.strptime(calendario, "%d-%m-%Y %H:%M:%S")
    if d.month == 12 and d.day <= 24:
        regalo_del_dia = d.day
        tiempo_restante = timedelta(hours=23, minutes=59,seconds=59) - timedelta(hours=d.hour, minutes=d.minute, seconds=d.second)
        return f"El regalo del día es: {lista_regalos[regalo_del_dia-1]} y el sorteo del día acaba en: {tiempo_restante}"
    
    elif d.month < 12:
        tiempo_faltante = datetime(year=2022, month=12, day=1) - d
        return f"El calendario de adviento 2022 comenzará en: {tiempo_faltante}"

    else:
        tiempo_sobrante = d - datetime(year=2022, month=12, day=24, hour=23, minute=59,second=59)  
        return f"El calendario de adviento 2022 ha finalizado hace: {tiempo_sobrante}"


print(encontrar_regalo("01-12-2022 18:46:00"))
print(encontrar_regalo("24-12-2022 18:00:00"))
print(encontrar_regalo("24-11-2022 13:00:00"))
print(encontrar_regalo("24-06-2022 00:00:00"))
print(encontrar_regalo("26-12-2022 13:00:00"))





