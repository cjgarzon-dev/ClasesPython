from abc import ABC, abstractmethod

# Clase abstracta
class Employee(ABC):
    def __init__(self, name, id, salary):
        self._name = name
        self._id = id
        self._salary = salary
        
    @property
    def name(self):
        return self._name    
    
    @property
    def id(self):
        return self._id
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, newSalary):
        if newSalary > 0:
            self._salary = newSalary
        else:
            raise ValueError('El salario debe ser mayor a 0')
    
    @abstractmethod
    def calculateBonus(self):
        pass
    
    def __str__(self):
        return f'Empleado: {self._name}, id: {self._id}, salario base: {self._salary}'      
        
class Development(Employee):
    def calculateBonus(self):
        return self._salary * 0.1
    
class Design(Employee):
    def calculateBonus(self):
        return self._salary * 0.05

class Managment(Employee):
    def calculateBonus(self):
        return 500

if __name__ == '__main__':
    dev = Development('Santiago', 123, 800)
    design = Design('Pepe', 321, 1000)
    managment = Managment('Carlos', 987, 2000)
    
    employees = [dev, design, managment]
    
    for employee in employees:
        print(employee)
        print(f'Bono: {employee.calculateBonus()}')