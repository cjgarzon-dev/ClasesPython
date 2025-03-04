from products import get_product

def calculate_total(list_product):
    """Calcular el total de la compra"""
    for product in list_product:
        total += product['price']
    return calculate_total

def add_product(id_product, cant, list_product):
    """Agregar un producto a la lista"""
    product = get_product(id_product)
    if product:
        list_product.append({'name': product['name'], 'price' : product['price'] * cant})
    else:
        raise ValueError(f'Producto con ID {id_product} no encontrado')           
