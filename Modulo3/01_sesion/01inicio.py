# CLASE EXCEPCIONES Y MANEJO DE ERRORES PYTHON _ 21/ENE/2025

# ESTRUCTURA GENERAL
'''
try:
    # Código
except AlgunaExcepcion as e:
    # Codigo

else:
    # Código

finally:        # acción que SIEMPRE se va a ejecutar
    # Codigo
'''

# Aplicación que permita dividir dos números
def divisionZero(num1, num2):
    try:
        result = num1/num2
        print(result)
    except ZeroDivisionError as e:
        print('La división por cero no se puede realizar')
        return None
divisionZero(2,0)


# EXCEPCIONES MULTIPLES
def divisionSecure():
    try:
        num1 = int(input('Ingrese el númerador: '))
        num2 = int(input('Ingrese el denominador: '))
        result = num1/num2
        print(f'El resultado de {num1}/{num2}={result}')
    except (ZeroDivisionError, ValueError) as e:
        print(f'Error: {e}')

#divisionSecure()

#EXCEPCIONES ESPECIFICAS -> NO ES RECOMENDABLE SIEMPRE YA QUE PUEDE ESCONDER ERRORES
def openFile():
    try:
        with open('datos.txt', 'r') as file:
            content = file.read()
            num = int(content.strip())      # quitar todos los espacios en blanco
            print(num)
    except Exception as e:
        print(f'Error: {e}')
openFile()


# USO DE ELSE Y FINALLY
def divisionComplete():
    try:
        num = int(input('Ingrese un numero: '))
        result = 10/num
    except ValueError as e:
        print(f'Error: {e}')
    except ZeroDivisionError as e:
        print(f'Error: {e}')
    else:
        print(f'El resultado de la división es: {result}')
    finally:                                
        print('La operación finalizó con éxito..')      # SIEMPRE SE VA A EJECUTAR
#divisionComplete()


# APP PROCESAR PEDIDO
def processingOrder():
    try:
        codProduct = input('Ingrese el codigo del producto: ')
        cant = int(input('Ingrese la cantidad del producto: '))
        
        if not codProduct.isalnum():        # VALIDAR QUE EL CODIGO DEL PRODUCTO SEA ALFANUMERICO
            raise ValueError('El codigo del producto debe ser alfanumérico')
        
        if cant <= 0:                    # VALIDAR QUE LA CANTIDAD SEA MAYOR A CERO
            raise ValueError('La cantidad del producto debe ser mayor a Cero')

        valueUnitary = 50
        total = valueUnitary * cant
        
    except ValueError as e:
        print(f'Error al procesar pedido {e}')
    else:
        print(f'Total a pagar: {total}')
    finally:
        print('Operacion finalizada')
#processingOrder()

# EXCEPCIONES PERSONALIZADAS
class ErrorPay(Exception):
    #Gestion de excepeciones
    pass

class PasarelaPay():
    #Simulación una estrategia tecnológica de pago
    
    @staticmethod
    def processPay(numTarget, amount):
        
        if not numTarget.startswith('4'):
            raise ErrorPay('El número de la tarjeta no es válido')
        
        if amount <= 0:
            raise ErrorPay('El monto debe ser mayor a cero')
        return f'El pago del monto ${amount} fue procesado con éxito'

def processPayClient(nameClient, numTarget, amount):
    try:
        print(f'Iniciando el proceso de pago para {nameClient}')
        result = PasarelaPay.processPay(numTarget, amount)
    except ErrorPay as e:
        print(f'Error al procesar el pago {e}')
    except Exception as e:
        print(f'Se produjo un error inesperado {e}')
    else:
        print(f'{result}')
    finally:
        print('Registro finalizada')
if __name__ == '__main__':
    processPayClient('Jose', '4ABC123', 99.80)
    processPayClient('Luis', '12345', 100)
    processPayClient('Maria', '45678', 0)