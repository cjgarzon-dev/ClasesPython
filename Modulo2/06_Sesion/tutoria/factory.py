# https://refactoring.guru/es
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def create(self):
        pass

class Car(Vehicle):
    def create(self):
        return 'Se creo un carro'
    
class Motorcycle(Vehicle):
    def create(self):
        return 'Se creo una moto'

class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicleType):
        if vehicleType == 'carro':
            return Car()
        elif vehicleType == 'moto':
            return Motorcycle()
        else:
            raise ValueError('Tipo de vehiculo desconocido')
        
try:
    factory = VehicleFactory()
    
    Car = factory.get_vehicle('carro')
    print(Car.create())
    
    Motorcycle = factory.get_vehicle('moto')
    print(Motorcycle.create())
    
    unknown = factory.get_vehicle('cicla')
except ValueError as e:
    print(e)