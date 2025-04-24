
products = {
    'XML0123': {'name': 'Manzana', 'price': 2000},
    'XML0124': {'name': 'Banano', 'price': 1800},
    'XML0125': {'name': 'Naranja', 'price': 1900},
    'XML0126': {'name': 'Pera', 'price': 2100},
    'XML0127': {'name': 'Uva', 'price': 2500},
    'XML0128': {'name': 'Sandía', 'price': 3000},
    'XML0129': {'name': 'Melón', 'price': 2800},
    'XML0130': {'name': 'Piña', 'price': 2700},
    'XML0131': {'name': 'Fresa', 'price': 2600},
    'XML0132': {'name': 'Kiwi', 'price': 3200},
    'XML0133': {'name': 'Mango', 'price': 3100},
    'XML0134': {'name': 'Papaya', 'price': 2900},
    'XML0135': {'name': 'Limón', 'price': 1700},
    'XML0136': {'name': 'Coco', 'price': 3500},
    'XML0137': {'name': 'Mandarina', 'price': 2000}
}

print(products['XML0123'])

class Product:
    def __init__(self, code: str, name: str, price: float):
        self.code = code
        self.name = name
        self.price = price
    
class Inventary:
    def __init__(self):
        self.products: dict[str, Product] = {}
    
    def add_product(self, product: Product):
        if product.code in self.products:
            print(f'El producto con código {product.code} ya existe')
        else:
            self.products[product.code] = product
            print(f'El producto con código {product.code} se agregó correctamente')
    
    def show_products(self):
        return {code: {'name': p.name, 'price': p.price} for code, p in self.products.items()}

class CashRegister:
    def __init__(self, inventary: Inventary):
        self.inventary = inventary
        self.sales: dict[str, float] = {}
    
    def shop(self, code_product: str, cant: int):
        if code_product not in self.inventary.products:
            print(f'El producto con código {code_product} no existe')
            return
            
        product = self.inventary.products[code_product]
        total = product.price * cant
        self.sales[code_product] = self.sales.get(code_product, 0) + total
        print(f'Compra realizada: {cant} x {product.name} = ${total}')
    
class MyStore:
    def __init__(self):
        self.inventary = Inventary()
        self.cash_register = CashRegister(self.inventary)
    
    def add_product(self, code: str, name: str, price: float):
        product = Product(code, name, price)
        self.inventary.add_product(product)
        
    def show_product(self):
        return self.inventary.show_products()
        
store_Paco = MyStore()
store_Paco.add_product('XML0123', 'Manzana', 2000)
store_Paco.add_product('XML0124', 'Banano', 1800)
store_Paco.add_product('XML0125', 'Naranja', 1900)
store_Paco.add_product('XML0126', 'Pera', 2100)
store_Paco.add_product('XML0127', 'Uva', 2500)
store_Paco.add_product('XML0128', 'Sandía', 3000)
store_Paco.add_product('XML0129', 'Melón', 2800)
store_Paco.add_product('XML0130', 'Piña', 2700)
store_Paco.add_product('XML0131', 'Fresa', 2600)
store_Paco.add_product('XML0132', 'Kiwi', 3200)
store_Paco.add_product('XML0133', 'Mango', 3100)
store_Paco.add_product('XML0134', 'Papaya', 2900)
store_Paco.add_product('XML0135', 'Limón', 1700)
store_Paco.add_product('XML0136', 'Coco', 3500)
store_Paco.add_product('XML0137', 'Mandarina', 2000)

print(store_Paco.show_product())

store_Paco.cash_register.shop('XML0137', 5)
store_Paco.cash_register.shop('XML01', 5)