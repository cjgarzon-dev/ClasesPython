class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        
    def move(self):
        print('El vehiculo ha comenzado a moverse')

class Car(Vehicle):
    def __init__(self, brand, motor, wheels):
        super().__init__(brand)
        self.motor = motor
        self.wheels = wheels
        
    def startTravel(self):
        self.motor.swichOn()
        for wheel in self.wheels:
            wheel.spin()
        self.move()
    
    def move(self):
        print('El carro ha comenzado a moverse')
        
class Motor:
    def __init__(self, type):
        self.type = type
        
    def swichOn(self):
        print(f'El motor de tipo {self.type} se ha encendido')
    
class Wheel:
    def __init__(self, size):
        self.size = size
        
    def spin(self):
        print(f'La rueda de tamaño {self.size} está girando')

motorSport = Motor('V18')

typeWheel = int(input('Elija el tipo de ruedas a usar (10-50): '))
wheelSmall = [Wheel(typeWheel), Wheel(typeWheel), Wheel(typeWheel), Wheel(typeWheel)]

vehicleSport = Car('Marca', motorSport, wheelSmall)
vehicleSport.startTravel()