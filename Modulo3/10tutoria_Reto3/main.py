import tkinter as tk
from tkinter import messagebox

# MODELO
class Product:
    def __init__(self, id_product, name, price, stock):
        self.id_product = id_product
        self.name = name
        self.price = price
        self.stock = stock
    
    def reduce_stock(self, cant):
        if cant < self.stock:
            self.stock -= cant
            return True
        return False

class Model:
    def __init__(self):
        self.products = {
            1: Product(1,'Manzana', 20, 100),
            2: Product(2, 'Pera', 15, 100),
            3: Product(3, 'Sandia', 10, 100),
            4: Product(4, 'Banano', 5, 100),
            5: Product(5, 'Maracuya', 15, 100),
            6: Product(6, 'Mandarina', 12, 100),
            7: Product(7, 'Mango', 25, 100),
            8: Product(8, 'Uva', 17, 100),
            9: Product(9, 'Limon', 8, 100),
            10: Product(10, 'Melon', 20, 100)
        }
        self.history_sales = []
    
    def obtain_product(self):
        return [f'{prod.id_product} - {prod.name} - ${prod.price} - Stock {prod.stock}' for prod in self.products.values()]

    def obtain_history(self):
        return self.history_sales
    
    def sale_product(self, id_product, cant):
        if id_product in self.products and self.products[id_product].reduce_stock(cant):
            total = self.products[id_product].price * cant
            self.history_sales.append((self.products[id_product].name, cant, total))
            return total
        return None

# CONTROLADOR
class Controller:
    def __init__(self):
        self.model = Model()
        
    def obtain_product(self):
        return self.model.obtain_product()

    def add_to_cart(self, product_str, cant, cart):
        id_product = int(product_str.split(' - ')[0])
        total = self.model.sale_product(id_product, cant)
        if total is not None:
            if id_product in cart:
                cart[id_product]['cant'] += cant
                cart[id_product]['total'] += total
            else:
                cart[id_product] = {'name': self.model.products[id_product].name, 'cant': cant, 'total': total}
        else:
            messagebox.showerror('Error', 'Stock insuficiente')
    
    def finalice_sale(self, cart, total_var):
        if not cart:
            messagebox.showerror('Error', 'El carrito está vacío')
            return
        message = 'Compra Finalizada'
        for id_product, total in cart.items():
            message += f'{self.model.products[id_product].name}: ${total}'
        messagebox.showinfo('Compra realizada', message)
        cart.clear()
        total_var.set('Total: $0')
    
    def show_history(self):
        pass

# VISTA
class View():
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title('Caja Registradora - Fruver')
        
        self.cart = {}
        self.total = tk.StringVar(value='Total: $0')
        self.cant_var = tk.StringVar()
        
        frame = tk.Frame(root)
        frame.pack()
        
        self.list_product = tk.Listbox(root)
        for prod in self.controller.obtain_product():
            self.list_product.insert(tk.END, prod)
        self.list_product.grid(row=0, column=0)
        
        self.list_cart = tk.Listbox(frame)
        self.list_cart.grid(row=0, column=1)
        
        tk.Entry(root, textvariable= self.cant_var).pack()
        
        tk.Button(root, text= 'Agregar', command= self.add_product).pack()
        tk.Button(root, text='Cancelar').pack()
        tk.Button(root, text='Finalizar Compra').pack()
        tk.Button(root, text='Ver historial').pack()
        
        tk.Label(root, textvariable=self.total).pack()
        
    def update_total(self):
        self.total.set(f'Total: ${sum(item['total'] for item in self.cart.values())}')
        self.update_cart()
    
    def update_cart(self):
        self.list_cart.delete(0, tk.END)
        for item in self.cart.values():
            self.list_cart.insert(tk.END, f'{item['name']} - {item['cant']} - ${item['total']}')
    
    def add_product(self):
        product = self.list_product.get(tk.ACTIVE)
        cant = self.cant_var.get()
        
        if cant.isdigit():
            cant = int(cant)
            self.controller.add_to_cart(product, cant, self.cart)
            self.update_total()
        else:
            messagebox.showerror('Error', 'Ingrese una cantidad válida')
        
# MAIN

root = tk.Tk()
controller = Controller()
app = View(root, controller)
root.mainloop()