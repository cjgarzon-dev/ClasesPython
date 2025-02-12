## Clase de Clases abstractas
## 05/12/2024

class Animal:                               # Clase ABSTRACTA
    
    def __init__(self):
        pass
    
    def speak(self):
        pass
    
class Dog(Animal):                          # INTERFAZ
    
    def __init__(self):
        pass
    
    def speak(self):
        return 'El perro hace Guau Guau'

class Cat(Animal):                          # INTERFAZ
    
    def __init__(self):
        pass
    
    def speak(self):
        return 'El gato hace miau miau'

animals = [Dog(), Cat(), Dog(), Cat()]

for animal in animals:
    print(animal.speak())
    
    
    