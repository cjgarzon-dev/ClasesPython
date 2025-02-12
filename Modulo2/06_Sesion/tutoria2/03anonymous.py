# CLASE ANONIMA
Product = type('Products', (),{'Name': None, 'Price': None})

product1 = Product()
product1.Name = 'Laptop'
product1.Price = 1000

print(f'Producto 1: {product1.Name}, Precio: {product1.Price}')