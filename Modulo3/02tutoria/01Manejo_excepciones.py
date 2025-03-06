# MANJEO DE EXCEPCIONES:

#* BLOQUE TRY
# EL BLOQUE TRY SE EJECUTA PARA ENVOLVER EL CODIGO QUE PUEDE GENERAR EXCEPCIONES.
# SI OCURRE UNA EXCEPCION SE EJECUTA EL BLOQUE EXCEPT
try:
    num = int(input('Ingrese un numero: '))
    print(f'El doble es: {num*2}')
    
except ValueError:
    print('No ingresaste un numero valido')
#* BLOQUE ELSE
# EL BLOQUE ELSE SE EJECUTA SOLO SI NO OCURRE NINGUNA EXCEPCION DENTRO DEL BLOQUE TRY    
else:
    print(f'El número ingresado es: {num}')
#* BLOQUE FINALLY
# EL BLOQUE FINALLY SE EJECUTA SIEMPRE, INDEPENDIENTEMENTE SI OCURRE O NO UNA EXCEPCION. ES UTIL PARA LIBERAL RECURSOS, CERRAR ARCHIVOS, CONEXIONES A DB
finally:
    print('Se terminó el programa')
    
try:
    file = open('archivo.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print('Error: El archivo no existe')
finally:
    try:
        file.close()
        print('Archivo cerrado')
    except NameError:
        print('El archivo no se abrio, no hay que cerrar')

#* MULTIPLES EXCEPCIONES
# Puedes manejar diferentes tipos de excepciones en el bloque separados por excepts
'''
try:
    num = int(input('ingresa un numero: '))
    result = 10/num
except ValueError:
    print('Error: no ingresaste un número válido')
except ZeroDivisionError:
    print('Error: No se puede dividir por cero') 
'''
try:
    num = int(input('ingresa un numero: '))
    result = 10/num
except (ValueError, ZeroDivisionError) as e:
    print(f'Error: {e}')

#* CREACION DE EXCEPCIONES PERSONALIZADAS

class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)
    
try:
    age = int(input('Ingrese su edad: '))
    if age < 0:
        raise MyException('La edad no puede ser negativa')
    print(f'SU edad es {age}')
except MyException as e:
    print(f'Error: {e}')

#! RECOMENDACIONES
# Use las excepciones sólo para situaciones excepcionales, no como lógica de control
# Siempre usar el 'finally' para liberar recursos
# Se especifica al capturar el error
# Documentar los procesos