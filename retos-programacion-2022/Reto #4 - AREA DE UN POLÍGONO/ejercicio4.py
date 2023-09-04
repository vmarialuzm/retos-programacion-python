from abc import ABC, abstractclassmethod

class Poligono(ABC):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    @abstractclassmethod
    def area(self):
        pass


class CalcularAreaTriangulo(Poligono):
    def area(self):
        area = self.base * self.altura / 2
        print(f"El area del triangulo es: {area}")


class CalcularAreaCuadrado(Poligono):
    def area(self):
        area = self.base * self.altura
        print(f"El area del cuadrado es: {area}")


class CalcularAreaRectangulo(Poligono):
    def area(self):
        area = self.base * self.altura
        print(f"El area del rectangulo es: {area}")


def area_poligono():
    triangulo = CalcularAreaTriangulo(10,20)
    triangulo.area()
    cuadrado = CalcularAreaCuadrado(10,20)
    cuadrado.area()
    rectangulo = CalcularAreaRectangulo(10,20)
    rectangulo.area()

area_poligono()


