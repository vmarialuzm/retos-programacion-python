import random

class CalendarSimulator:
    def __init__(self):
        self.participantes=[]
    
    def añadir_participante(self):
        participante = input("Ingrese el nombre del participante: ")

        if participante in self.participantes :
            print(f"Participante {participante} ya existe") 
        else:
            self.participantes.append(participante)
            print(f"Participante {participante} añadido exitosamente") 

    def mostrar_participantes(self):
        print("Listado de participantes")
        for participante in self.participantes:
            print(participante)

    def eliminar_participante(self):
        participante = input("Ingrese el nombre del participante a eliminar: ")
        if participante in self.participantes:
            self.participantes.remove(participante)
            print(f"Participante {participante} eliminado exitosamente") 
        else:
            print(f"El nombre {participante} no existe")

    def realizar_sorteo(self):
        persona_al_azar = random.choice(self.participantes)
        self.participantes.remove(persona_al_azar)
        print(f"Sorteo realizado, la persona eliminada fue {persona_al_azar}")

def menu():

    calendario = CalendarSimulator()

    while True:
        
        print("Menú de opciones: ")
        print("1. Añadir participante")
        print("2. Mostrar participantes")
        print("3. Eliminar participante")
        print("4. Realizar sorteo")
        print("5. Salir")

        eleccion = input("Ingrese el número de acción a realizar: ")

        print("************************************************************************")

        if eleccion == "1":
            calendario.añadir_participante()
        
        elif eleccion == "2":
            calendario.mostrar_participantes()
        
        elif eleccion == "3":
            calendario.eliminar_participante()

        elif eleccion == "4":
            calendario.realizar_sorteo()
        
        elif eleccion == "5":
            print("Gracias por participar...")
            break


if __name__ == '__main__':
    menu()