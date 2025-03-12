import tkinter as tk
from tkinter import messagebox, ttk

class ViewStore:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title('Caja Registradora - Tienda Fruver')
        self.configure_interfaz()
        self.load_products()
        self.root_mainloop()
    
    def configure_interfaz(self):
        self.treeview_products = ttk.Treeview(self.root, columns=('Products', 'Price', 'Cant_Available'), show='headings', height=10)
        self.treeview_products.heading('Products', text='Producto')
        self.treeview_products.heading('Price', text='Precio')
        self.treeview_products.heading('Cant_Available', text='Cantidad Disponible')

        self.entry_cant = tk.Entry(self.root)
        self.entry_cant.pack()
        
        self.button_add = tk.Button(self.root, text='Agregar', command=self.add_products)
        self.button_add.pack()
        
        self.button_finalice = tk.Button(self.root, text='Finalizar Compra', command=self.controller.finalize_sale)
        self.button_finalice.pack()
    
    def load_products(self):
        for id_product, product in self.controller.obtain_product().items():
            self.treeview_products.insert('', 'end', iid= str(id_product), values= (product.name, product.price, product.stock))
    
    def add_products(self):
        try:
            selected_item = self.treeview_products.selection()[0]
            id_product = int(selected_item)
            cant = int(self.entry_cant.get())
            self.controller.add_to_cart(id_product, cant)
            messagebox.showinfo('Exito', 'Producto agregado con éxito')
        except:
            messagebox.showerror('Error')
    