# IMPLEMENTAR UN SISTEMA DE MONITOREO PARA FACTURACIÓN, CON MANEJO DE EXCEPCIONES POR CONSOLA Y LOG.FILE

import logging
from dataclasses import dataclass

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filename = 'ejercicio2.log',
    filemode = 'w'
)

# CREAR UN NUEVO HANDLER PARA GESTIONAR MENSAJES DE AUDITORIA POR .LOG Y CONSOLA
console_Handler = logging.StreamHandler()       # CREAR UNA INSTANCIA, ES DECIR, UN NUEVO MANEJADOR
console_Handler.setLevel(logging.DEBUG)         # CONFIGURAR EL NIVEL DEL LOGGING, EN ESTE CASO EL NIVEL MAS LEVEL
console_Handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))    # DANDO FORMATO A LA SALIDA DEL LOGGING
logging.getLogger().addHandler(console_Handler) # AGREGANDO LA INSTANCIA console_handler AL MANEJADOR PRINCIPAL

@dataclass
class Bill:
    client : str
    cant : int
    priceUnit : float
    
    def process(self):
        try:
            logging.info(f'Iniciando el proceso de facturación para el cliente {self.client}')
            
            if self.cant <= 0:
                raise ValueError('La cantidad del producto debe ser mayor a cero')
            if self.priceUnit <= 0:
                raise ValueError('El precio debe ser mayor a cero')
            
            total = self.cant * self.priceUnit
            logging.info(f'Factura procesada con éxito. Precio total de la compra ${total} - Cliente: {self.client}')
            
        except ValueError as e:
            logging.error(f'Error de validación del cliente {self.client}: {e}')
        except Exception as e:
            logging.critical(f'Error inesperado al momento de procesar la factura del cliente {self.client}: {e}')
        finally:
            logging.info(f'El proceso de facturación para el cliente {self.client} finalizó')
if __name__ == '__main__':
    bill1 = Bill('Carlos', 2, 1500.25)
    bill1.process()
    
    bill2 = Bill('Pedro', 2, 250)
    bill2.process()
    
    bill3 = Bill('Pedro', 2, 250)
    bill3.process()