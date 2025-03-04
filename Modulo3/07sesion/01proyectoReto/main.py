import tkinter as tk
from tkinter import messagebox, ttk
from operations import add_product, calculate_total
from exceptions import manage_errors
from products import products, history_sales

products_selected = []

def add_since_list():
    try:
        selected_item = treeview_products.selection()
        if not selected_item:
            raise ValueError('Debe seleccionar un producto de la lista')
        
        id_product = selected_item[0]
        
        if not id_product.isdigit() or int(id_product) not in products:
            raise ValueError('ID de producto no válido')
        
        cant = int(entry_cant.get())

def update_list():
    for row in treeview_selected.get_children():
        treeview_selected.delete(row)
    for product in products_selected:
        treeview_selected.insert('', 'end', values=(product['name'], f'${product['price']:.2f}'))
    total = calculate_total(products_selected)
    tag_total.config(text=f'Total: ${total:.2f}')
    
def finish_buy():
    total = calculate_total(products_selected)
    bill_text = 'RECIBO DE COMPRA\n\n'
    bill_text += '-' * 30 + '\n'
    
    for product in products_selected:
        bill_text += f'{product['name']} - ${product['price']:.2f}\n'
    
    for product in products_selected:
        history_sales.append({
            'product' : product['name'],
            'cant' : 1,
            'price_total' : product['price']
        })
    
    bill_text += '-' * 30 + '\n'
    bill_text += f'Total: ${total:.2f}\n'
    bill_text += '-' * 30
    messagebox.showinfo('Recibo de Compra', bill_text)
    
    products_selected.clear()
    update_list()

def show_historial():
    history_sales = tk.Toplevel(window)
    history_sales.title('Historial de Ventas')
    
    treeview_history = ttk.Treeview(history_sales, columns=('Producto', 'Cantidad', 'Precio Total'), show='headings', height=10)
    treeview_history.heading('Producto', text='Producto')
    treeview_history.heading('Cantidad', text='Cantidad')
    treeview_history.heading('Precio Total', text='Precio Total')
    treeview_history.heading('Producto', width=200)
    treeview_history.heading('Cantidad', width=100)
    treeview_history.heading('Precio Total', width=150)
    
    for sale in history_sales:
        treeview_history.insert('', 'end', values=(sale['product'], sale['cant'], f'${sale['price_total']:.2f}'))
        
    treeview_history.pack(padx=20, pady=20)
    
    # MOSTRAR GANANCIAS TOTALES
    earnings_totals = sum(sale['price_total'] for sale in history_sales)
    tag_earnings = tk.Label(history_sales, text=f'Ganancias totales: ${earnings_totals:.2f}', font=('Arial', 14, 'bold'))
    tag_earnings.pack(pady=10)
    
    