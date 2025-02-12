# CLASES ABSTRACTAS EN PYTHON
from abc import ABC, abstractmethod

class Form(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

class Circle(Form):
    
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return f'El área de un Círculo es: {3.14 * self.radio ** 2}'
    
    def perimeter(self):
        return f'El perímetro de un círculo es: {2 * 3.14 * self.radio}'

class Rectangle(Form):
    
    def __init__(self, base, high):
        self.base = base
        self.high = high
        
    def area(self):
        return f'El área de un rectángulo es: {self.base * self.high}'
    
    def perimeter(self):
        return f'El perímetro de un rectángulo es: {2*(self.base+self.high)}'
    
class Quadrate(Form):
    
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return f'El área de un cuadrado es {self.side**2}'
    
forms = [
    Circle(5),
    Rectangle(2,10),
    Quadrate(8),
    Rectangle(10,20),
    Circle(22)
]

print('Area de las formas:')
for form in forms:
    print(form.area())
    
circle1 = Circle(5)
rectangule1 = Rectangle(2,4)
print('Perímetros de las formas:')
print(circle1.perimeter())
print(rectangule1.perimeter())