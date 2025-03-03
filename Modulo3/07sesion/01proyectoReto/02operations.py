# DATA QUEMADA -> DICCIONARIO
products = {
    1: {'name': 'Manzana', 'price': 1.5, 'stock': 100},
    2: {'name': 'Plátano', 'price': 1.0, 'stock': 150},
    3: {'name': 'Pera', 'price': 2.0, 'stock': 80},
    4: {'name': 'Uva', 'price': 2.5, 'stock': 120},
    5: {'name': 'Sandía', 'price': 3.0, 'stock': 50},
    6: {'name': 'Melón', 'price': 2.8, 'stock': 60},
    7: {'name': 'Naranja', 'price': 1.2, 'stock': 200},
    8: {'name': 'Mandarina', 'price': 1.3, 'stock': 180},
    9: {'name': 'Kiwi', 'price': 3.5, 'stock': 70},
    10: {'name': 'Fresa', 'price': 2.8, 'stock': 90},
    11: {'name': 'Aguacate', 'price': 2.2, 'stock': 110},
    12: {'name': 'Papaya', 'price': 2.6, 'stock': 40},
    13: {'name': 'Granada', 'price': 3.2, 'stock': 75},
    14: {'name': 'Cereza', 'price': 4.0, 'stock': 85},
    15: {'name': 'Frambuesa', 'price': 3.7, 'stock': 65},
    16: {'name': 'Plátano macho', 'price': 1.8, 'stock': 95},
    17: {'name': 'Piña', 'price': 3.5, 'stock': 55},
    18: {'name': 'Mango', 'price': 2.5, 'stock': 105},
    19: {'name': 'Lima', 'price': 1.0, 'stock': 130},
    20: {'name': 'Limón', 'price': 1.0, 'stock': 140},
}

# HISTORIAL DE VENTAS
history_sales = []

def get_product(id_product):
    return products.get(id_product, None)

def calculate_total(list_products):
    """Calcular el total del a compra"""
    total = 0
    for product in list_products:
        total += product['price']
    return total

def add_products(id_product, cant, list_prodcuts):
    """Agregar un producto a la lista de compra y registrar una venta"""
    product = get_product(id_product)
    if product:
        list_prodcuts.append({'name': product['name'], 'price': product['price'] * cant})
        
        # REGISTRAR UNA VENTA EN EL HISTORIAL
        history_sales.append({
            'product' : product['name'],
            'cant' : cant,
            'price_total' : product['price'] * cant
        })
    else:
        raise ValueError(f'Producto con ID {id_product} no encontradp')