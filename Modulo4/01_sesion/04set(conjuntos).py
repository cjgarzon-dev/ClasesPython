# Conjuntos (SET) en python
# App de gestión de clientes (únicos) de una campaña de mercadeo

from typing import Set

def obtain_clients_only(clients: Set[str], new_clients: Set[str]) -> Set[str]:
    return clients.union(new_clients)

def management_clients(clients: Set[str]) -> None:
    
    # Agregar un cliente:
    clients.add('Pedro')
    print('Clientes después de agregar a Pedro: ', clients)
    
    # Agregar a un cliente duplicado:
    clients.add('Carlos')
    print('Clientes después de intentar agregar a Carlos: ', clients)
    
    # Uso de la función 'remove' para eliminar un cliente (si existe el cliente y si no => error):
    clients.remove('Ana')
    print('Clientes después de eliminar a Ana con el método remove: ', clients)
    
    # Uso de la función 'discard' para eliminar un elemento del set:
    clients.discard('Luis')
    print('Clientes después de eliminar a Luis con el método discard: ', clients)
    
    # Uso del método para mostrar un elemento del set y posterior lo borra automáticamente
    client_remove = clients.pop()
    print(f'Cliente removido aleatoriamente {client_remove}')
    print('Clientes restantes: ', clients)
    
    # Borrar todos los elementos del set:
    clients.clear()
    print('Clientes después del método Clear: ', clients)

def main():
    
    clients_old = {'Carlos', 'Ana', 'Luis'}
    clients_new = {'Luis', 'Maria', 'Jorge'}
    clients_finaly = obtain_clients_only(clients_old, clients_new)
    print('La lista actualizada de clientes es: ', clients_finaly)
    
    management_clients(clients_finaly)

if __name__ == '__main__':
    main()