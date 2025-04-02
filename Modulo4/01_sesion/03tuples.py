# App: para registro de empleados
# Las tuplas poseen un índice, son inmutables, permite valores duplicados
from typing import Tuple

def get_info_employee(employee: Tuple[int, str, str]) -> Tuple:
    id_employee, name_employee, job_employee = employee
    print(f'Id: {id_employee}, Nombre: {name_employee}, Cargo: {job_employee}')

def analize_salary(salary: Tuple[int, ...]) -> None:            # al colocar ... se menciona que los valores que siguen serán enteros
    
    print(f'Salarios tabulados: {salary}')
    print(f'Cantidad de salarios registrados: {len(salary)}')
    print(f'El salario mas alto registrado es: {max(salary)}')
    print(f'El salario mas bajo registrado es: {min(salary)}')
    print(f'La suma de todos los salarios registrados es: {sum(salary)}')
    print(f'Los salarios registardos de forma ordenada: {sorted(salary)}')
    
    salary_to_find = 500
    print(f'El salario con un valor de ${salary_to_find} se encuentra {salary.count(salary_to_find)} veces')
    
    if salary_to_find in salary:
        print(f'El salario con un valor de ${salary_to_find} se encuentra en la posición {salary.index(salary_to_find)}')
        
def main():
    employee1 = (12345, 'Carlos Perez', 'Director Comercial')
    
    get_info_employee(employee1)
    
    salary_employees = (500, 500, 100, 200, 300, 400, 500, 600)
    
    analize_salary(salary_employees)

if __name__ == '__main__':
    main() 
