class Product:
    def __init__(self, id_product, name, price, stock):
        self.id_product = id_product
        self.name = name
        self.price = price
        self.stock = stock
        
    def reduce_stock(self, cant):
        if cant > self.stock:
            raise ValueError('Stock suficiente')
        self.stock -= cant
    
class Store:
    def __init__(self):
        self.products = {}
        self.history_sales = []
        
    def add_products(self, id_product, name, price, stock):
        self.products[id_product] = Product(id_product, name, price, stock)
        
    def obtain_product(self, id_product):
        return self.products.get(id_product)
    
    def register_sale(self, id_product, cant):
        product = self.obtain_product(id_product)
        
        if product:
            product.reduce_stock(cant)
            total = product.price * cant
            self.history_sales.append({
                'product': product['name'],
                'cant': cant,
                'price_total': total
            })
        else:
            raise ValueError(f'Producto no encontrado')