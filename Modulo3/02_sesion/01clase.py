# CLASE DE LOGS Y DEPURACION - 23/ENE/25

# EXCEPCIONES PERSONALIZADAS
class ErrorPay(Exception):
    #Gestion de excepeciones
    pass

class PasarelaPay():
    #Simulación una estrategia tecnológica de pago
    
    @staticmethod
    def processPay(numTarget, amount):
        
        if not numTarget.startwith('4'):
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