## Listas en python
products = ['carne', 'papa', 'tomate']
products.append('yuca')
print(products)

## Tuplas en python
employees = (1010, 'Luis', 'Director', 1500000)
print(employees)
#employees[1] = 'Camilo'         # No se puede cambiar los datos ya que las tuplas son inmutables.
#print(employees)

## Set (conjuntos) en python
categories = {'Terror', 'Drama', 'ScFc'}
categories.add('Suspenso')
print(categories)

## Diccionarios (dict) en python
clients = {
    'id': 1010,
    'name': 'Luis',
    'last_name': 'Morelos'
}
print(clients)
clients['email'] = 'lmorelos@gmail.com'
print(clients)