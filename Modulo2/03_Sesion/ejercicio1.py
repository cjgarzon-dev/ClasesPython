# Ejercicio 1: Clase abstracta de figura geométrica
# Crea una clase abstracta Figura con un método abstracto area. Luego, implementa clases concretas Cuadrado y Rectángulo que calculen el área.

from abc import ABC, abstractmethod

class Figure(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
class Quadrate(Figure):
    
    def __init__(self, slide):
        self.slide = slide
        
    def area(self):
        return f'El área de un cuadrado es: {self.slide**2}'
    
    def perimeter(self):
        return f'El perímetro de un cuadrado es: {4*self.slide}'

class Rectangle(Figure):
    
    def __init__(self, base, high):
        self.base = base
        self.high = high
        
    def area(self):
        return f'El área de un rectángulo es: {self.base*self.high}'

quadrate1 = Quadrate(2)
print(quadrate1.area())
print(quadrate1.perimeter())

rectangle1 = Rectangle(4,3)
print(rectangle1.area())