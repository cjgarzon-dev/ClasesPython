class Vehicle:
    
    def __init__(self, motor):
        self.motor = motor
    
    def swichOn(self):
        print('Encendiendo el vehículo de')
        self.motor.start()

class Motor:
    
    def __init__(self):
        pass
    
    def start(self):
        pass

class MotorGasoline(Motor):
    
    def __init__(self):
        pass
    
    def start(self):
        print(f'Motor a Gasolina')
    
class MotorElectric(Motor):
    
    def __init__(self):
        pass
    
    def start(self):
        print(f'Motor Electrico')

motorGasoline = MotorGasoline()
motorElectric = MotorElectric()

car_gasoline = Vehicle(motorGasoline)
car_electric = Vehicle(motorElectric)

car_gasoline.swichOn()
car_electric.swichOn()

    
