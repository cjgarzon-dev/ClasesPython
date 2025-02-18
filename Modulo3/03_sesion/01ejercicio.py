# USO DE BREAKPOINT SIMPLE

class Employee:
    def __init__(self, name, sales):
        self.name = name
        self.sales = sales
    
    def calculateCommission(self):
        if self.sales > 5000:
            print(f'***Empleado: {self.name}. Ventas: {self.sales}. Comisión del 10%')
            return self.sales * 0.1
        print(f'***Empleado: {self.name}. Ventas: {self.sales}. Comisión del 5%')
        return self.sales * 0.05
    
employess = [
    Employee('Ana', 6000),
    Employee('Luis', 3000)
]

for employee in employess:
    print(f'Empleado: {employee.name}. Comisión: ${employee.calculateCommission()}')