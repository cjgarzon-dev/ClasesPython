# Ejercicio 2: Polimorfismo con animales
# Crea una clase Animal con un método hacer_sonido. Implementa dos clases derivadas, Perro y Gato, que sobrescriban este método.

class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def makeSound(self):
        pass

class Dog(Animal):
    
    def __init__(self, name):
        super().__init__(name)
    
    def makeSound(self):
        return f'El perro {self.name} hace guau guau'

class Cat(Animal):
    
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def makeSound(self):
        return f'El gato de color {self.color} hace miau miau'

animals = [Dog('Pepe'), Cat('Juancho', 'Negro')]
for animal in animals:
    print(animal.makeSound())
cat1 = Cat('Oscar', 'Negro')
print(cat1.makeSound())
dog1 = Dog('Juancho')
print(dog1.makeSound())