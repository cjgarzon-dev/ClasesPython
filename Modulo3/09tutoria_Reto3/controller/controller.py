from tkinter import messagebox
from View.view import ViewStore

class ControllerStore:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.cart = []
        
    def obtain_products(self):
        return self.model.products
    
    def add_to_cart(self, id_product, cant):
        product = self.model.obtain_product(id_product)
        if product:
            if cant > product.stock:
                raise ValueError('Stock insuficiente')
            self.cart.append({'product': product.name, 'cant': cant, 'price_total': product.price * cant})
        else:
            raise ValueError('Producto no encontrado')
    
    def finalize_sale(self):
        total = sum(item['price_total'] for item in self.cart)
        messagebox.showinfo('Compra finalizada', f'Total: ${total:.2f}')
        
        for item in self.cart:
            product_id = next((p_id for p_id, p in self.model.products.items() if p.name == item['product']), None)
            if product_id is not None:
                self.model.register_sale(product_id, item['cant'])
            else:
                messagebox.showerror('Error', 'Producto no encontrado en la tienda')
        
        self.view.update_view_products()
        self.cart.clear()