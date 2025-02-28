# CLASE 6: RESOLUCION Y DEPURACION DE PROBLEMAS COMUNES _ 07/FEB/2025

import pdb
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Employee(ABC):
    name : str
    salaryBase : float
    
    @abstractmethod
    def calculateSalary(self):
        pass

@dataclass
class Manager(Employee):
    def calculateSalary(self):
        return self.salaryBase + 5000

class Developer(Employee):
    def calculateSalary(self):
        return self.salaryBase + 2000

def calculate_total_salary(employee: Employee) -> float:
    return employee.calculateSalary()
    
if __name__ == '__main__':
    manager = Manager('Pascual', 30000)
    developer = Developer('Jacinta', 25000)
    print(calculate_total_salary(manager))
    print(calculate_total_salary(developer))