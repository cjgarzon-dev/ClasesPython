products = [
    {'name': 'Laptop', 'price': 1000},
    {'name': 'Celular', 'price': 800},
    {'name': 'Tablet', 'price': 600}
]

products_Filter = filter(lambda x: x['price']<1000, products)

products_Ordered = sorted(products_Filter, key=lambda x: x['price'])
print(products_Ordered)
