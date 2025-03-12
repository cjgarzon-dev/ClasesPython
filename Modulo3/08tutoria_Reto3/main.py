'''
Desarrollar una aplicación de escritorio que permita:
Seleccionar productos desde una lista.Especificar la cantidad a comprar.
Verificar  la  disponibilidad  del  producto  antes  de  añadirlo  a  lacompra.
Calcular el total de la compra en tiempo real.Registrar el historial de ventas y mostrarlo en pantalla.
Gestionar correctamente la actualización del stock de productos.
'''

# Libreria -> Es una colección de código desarrollada previamente, busca agilziar el desarollo (datetime, dataclass, tkinter, pandas, matploitlib)
# Framework -> Es un marco de trabajom, es decir, plantillas, buscan que el código sea mas rápido y eficiente. Especialmente para Backend (Django _ Flask _ React)

import tkinter as tk
from tkinter import messagebox, ttk
from operations import obtain_products, add_product_history, calculate_total
from exceptions import manage_error
from products import products

# Configurar la Interfaz
root = tk.Tk()
root.title('Caja Registradora - Tienda Fruber')

# Marco principal
frame_principal = tk.Frame(root, padx=30, pady=30, bg='#f4f4f9')
frame_principal.pack(fill='both', expand=True)

#Titulo
tittle = tk.Label(frame_principal, text='Bienvendido a la tienda Fruver', font=('Arial', 20), bg='#f4f4f9', fg='green')
tittle.grid(row=0, column=0, padx=10, pady=10)

#Frame para lista de productos
frame_products = tk.Frame(frame_principal,bg='#f4f4f9')
frame_products.grid(row=1, column=0, padx=10, pady=10)

# Frame para equiopos
tag_list_equipments = tk.Label(frame_products, text= 'Selecciona un producto', font=('Arial', 14), bg='#f4f4f9', fg='green')
tag_list_equipments.pack(pady=10)

treeview_products = ttk.Treeview(frame_products, columns=('Products', 'Price', 'Cant_Available'), show='headings', height=10)
treeview_products.heading('Products', text='Producto')
treeview_products.heading('Price', text='Precio')
treeview_products.heading('Cant_Available', text='Cantidad Disponible')
treeview_products.column('Products')
treeview_products.column('Price')
treeview_products.column('Cant_Available')

# Inserta productos en el Treeview
for key, product in products.items():
    cant_available = 100
    treeview_products.insert('', 'end', iid= str(key), values=(product['name'], f'${product['price']}', cant_available))

treeview_products.pack(pady=10)

# Frame para la cantidad y el boton
frame_cant = tk.Frame(frame_principal, bg='#f4f4f9')
frame_cant.grid(row=1, column=1, padx=10, pady=10)

# Campo para la cantidad
tag_cant = tk.Label(frame_cant, text= 'Cantidad', font= ('Arial', 14), bg= '#f4f4f9')
tag_cant.pack(pady=10)

for p in products.items():
    print(p)
    
root.mainloop()