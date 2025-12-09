from controllers.estudiante_control import EstudianteControl
from mysql.connector import IntegrityError

def menu_principal(db):

    estudiante_control = EstudianteControl(db)

    while True:
        print("Bienvenido a la Academia")
        print("1. Registrar Estudiante")
        print("2. Listar Estudiantes")
        print("3. Salir") 
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_estudiante(estudiante_control)
        elif opcion == '2':
            listar_estudiantes(estudiante_control)
        elif opcion == '3':
            print("Saliendo del programa.")
            break
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

def listar_estudiantes(estudiante_control):
    print("+++++++++++++ Listar Estudiantes +++++++++++++")
    try:
        estudiantes = estudiante_control.listar_estudiantes()
        if estudiantes:
            print("ID | Nombre | Apellido | Correo Electrónico | Teléfono")
            for est in estudiantes:
                print(f"{est.id_estudiante} | {est.nombre} | {est.apellido} | {est.correo_electronico} | {est.telefono}")
        else:
            print("No hay estudiantes registrados.")
    except Exception as e:
        print(f"Error al listar los estudiantes: {str(e)}")