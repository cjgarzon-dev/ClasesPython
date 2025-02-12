## Clase de Composición vs Herencia y mejores prácticas
## 12/12/2024

class Vehicle:
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def description(self):
        return f'El vehículo es de marca {self.make} y modelo {self.model}'
    
class Car(Vehicle):
    
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def description(self):
        return f'El vehículo es de marca {self.make}, modelo {self.model} y tiene {self.doors} puertas'

myCar1 = Car('Chevrolet', 'Sedan', 3)
print(myCar1.description())

 