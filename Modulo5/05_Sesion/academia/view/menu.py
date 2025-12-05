from controllers.estudiante_control import EstudianteControl
from mysql.connector import IntegrityError

def menu_principal(db):

    estudiante_control = EstudianteControl(db)

    print("Bienvenido a la Academia")
    print("1. Registrar Estudiante")
    print("2. Salir") 
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_estudiante(estudiante_control)
    elif opcion == '2':
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Intente de nuevo.")
    
def registrar_estudiante(estudiante_control):
    print("+++++++++++++ Registrar Estudiante +++++++++++++")
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    correo_electronico = input("Ingrese el correo electrónico del estudiante: ")
    telefono = input("Ingrese el teléfono del estudiante: ")
    try:
        estudiante_control.registrar_estudiante(nombre, apellido, correo_electronico, telefono)
        print("Estudiante registrado exitosamente.")
    except IntegrityError as e:
        print(f"Error de integridad al registrar el estudiante: {e.msg}")
    except Exception as e:
        print(f"Error al registrar el estudiante: {e.msg}")
    finally:
        print("++++++++++++++++++++++++++++++++++++++++++++++")
        print("Registro de estudiante finalizado.")
        menu_principal(estudiante_control.db)