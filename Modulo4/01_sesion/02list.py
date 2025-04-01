# App: gestión de pedidos de una tienda

def add_order(orders: list[str], new_order: str) -> list[str]:
    orders.append(new_order)
    return orders
def remove_order(orders: list[str], order_to_remove: str) -> list[str]:
    if order_to_remove in orders:
        orders.remove(order_to_remove)
    else:
        print('Pedido no se encuentra en lista')
    return orders

def find_order(orders: list[str], order_to_find: str) -> int:
    if order_to_find in orders:
        return orders.index(order_to_find)
    else:
        print('Pedido no encontrado en la lista')
        return -1
    
def main():
    # Lista inicial de pedidos:
    orders = ['Order 1', 'Order 3', 'Order 4']
    
    # Agregar un nuevo pedido a la lista
    orders = add_order(orders, 'Order 2')
    
    # Mostrar los elementos de la lista
    print('Lista actualizada de pedidos', orders)
    
    # Ordenar pedidos lista
    orders.sort()
    print('Lista ordenada de pedidos', orders)
    
    # Buscar un pedido en específico
    order_to_find = 'Order 3'
    index = find_order(orders, order_to_find)
    if index != -1:
        print(f'El {order_to_find} se encuentra en la posición {index}')
    
    # Eliminar un pedido
    order_to_remove = 'Order 1'
    orders = remove_order(orders, order_to_remove)
    print(f'Lista resultante luego de eliminar a {order_to_remove}: {orders}')

if __name__ == '__main__':
    main()