from products import products, history_sales

def obtain_products(id_product):
    return products.get(id_product, None)

def add_product_history(id_product, cant, list_product):
    product = obtain_products(id_product)
    if products:
        list_product.append({'name': product['name'], 'price': product['price'] * cant})
        
        history_sales.append({
            'product': product['name'],
            'cant': product[cant],
            'price_total': product['price'] * cant
            })
    else:
        raise ValueError(f'Producto con id {id_product} no encontrado')
    
def calculate_total(list_product):
    total = 0
    for product in list_product:
        total += product['price']
    return total