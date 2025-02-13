# CLASE DE LOGS Y DEPURACION - 23/ENE/25
#Los logs son registros de eventos 

import logging
from dataclasses import dataclass, field

'''
#ESTRUCTURA BASICA
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug('Este mensaje es del DEBUG')
logging.info('Este mensaje es del INFO')
logging.warning('Este mensaje es del WARNING')
logging.error('Este mensaje es del ERROR')
logging.critical('Este mensaje es del CRITICAL')
'''

# APP QUE PERMITE LLEVAR SEGUIMIENTOS DE COMPRAS Y FALLOS EN EL PROCESO DE TRANSACCION
# ESTA APP REGISTRARÁ LA CANTIDAD DE PRODUCTOR COMPRADOS, CONFIRMACIOND DE COMPRA Y ERRORES EN ESTA TRANSACCION

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='register.log',
    filemode='a'
)

@dataclass
class Product:
    name : str
    price : float
    cant : int
    
    def buy(self, cant : int):
        if cant > self.cant:
            logging.error(f'Error: No hay suficiente cantidad del producto {self.name}. El stock disponible es de {self.cant}')
            print(f'Error: No hay suficiente cantidad del producto {self.name}. El stock disponible es de {self.cant}')
            raise ValueError(f'Error: No hay suficiente cantidad del producto {self.name}. El stock disponible es de {self.cant}')
        else:
            self.cant -= cant
            logging.info(f'La compra fué exitosa. El stock restante es {self.cant}')
            print(f'La compra fué exitosa. El stock restante es {self.cant}')
            return self.price * cant

@dataclass
class Store:
    products: list[Product] = field(default_factory=list)
    
    def addProduct(self, product:Product):
        self.products.append(product)
        logging.debug(f'Producto {product.name} agregado con éxito. El precio es de {product.price} - Cantidad: {product.cant} unidades en stock')
        print(f'Producto {product.name} agregado con éxito. El precio es de {product.price} - Cantidad: {product.cant} unidades en stock')
    
    def realiceBuy(self, nameProduct:str, cant:int):
        product = next((p for p in self.products if p.name == nameProduct), None)
        if product:
            try:
                total = product.buy(cant)
                logging.info(f'Compra realizada: {cant} unidades de {nameProduct} por un total de ${total}')
                print(f'Compra realizada: {cant} unidades de {nameProduct} por un total de ${total}')
                return total
            except ValueError as e:
                logging.error(f'Error al efectuar la compra: {e}')
                print(f'Error al efectuar la compra: {e}')
        else:
            logging.warning(f'Producto fuera de stock')
            print(f'Producto fuera de stock')

if __name__ == '__main__':
    store = Store()
    
    inventaryLaptop = Product(name='Portatil', price=1000, cant=10)
    store.addProduct(inventaryLaptop)
    store.realiceBuy('Portatil', 4)        
    
    inventaryKeyboard = Product(name='Teclado', price=50, cant=5)
    store.addProduct(inventaryKeyboard)
    store.realiceBuy('Teclado', 10) 