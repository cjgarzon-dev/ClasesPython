import tkinter as tk
from tkinter import messagebox

products = {
    1: {'name': 'Manzana', 'price': 3.5, 'stock': 100},
    2: {'name': 'Pera', 'price': 2.5, 'stock': 100},
    3: {'name': 'Sandia', 'price': 1.5, 'stock': 100}
}

history_sales = []

def get_product(id_product):
    return products.get(id_product)

def add_product(id_product, cant, list_product):
    try:
        id_product = int()
        product = get_product(id_product)
        
        if product:
            if cant <= product['stock']:
                history_sales.append({product})
    except:
        print('una excepcion ocurrió')

def update_list():
    list_products.delete(0, tk.END)
    for id_product, date in products.items():
        list_products.insert(tk.END, f'{id_product}: {date['name']} - ${date['price']} - Stock: {date['stock']}')
        
        
root = tk.Tk()
root.title('Tienda')

frame = tk.Frame(root)
frame.pack(padx=10)

list_products = tk.Listbox(frame, width=40)
list_products.pack()
update_list()

frame_inputs = tk.Frame(root)
frame_inputs.pack(padx=10)

tk.Label(frame_inputs, text=('ID Producto:')).grid(row=0, column=0)
entry_id = tk.Entry(frame_inputs)
entry_id.grid(row=0, column=1)

root.mainloop()