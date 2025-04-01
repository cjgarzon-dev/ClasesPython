# App: para registro de empleados

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
