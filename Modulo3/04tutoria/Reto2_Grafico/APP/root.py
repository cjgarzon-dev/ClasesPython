import tkinter as tk
from tkinter import messagebox, ttk
from APP.controller_client import Controller_Client

class Root:
    def __init__(self):
        self.controller_client = Controller_Client()
        self.root = tk.Tk()
        self.root.title('Sistema Gestión Veterinaria')

        self.label_client = tk.Label(self.root, text= 'Nombre Cliente: ')
        self.label_client.grid(row=0, column=0)
        self.entry_client = tk.Entry(self.root)
        self.entry_client.grid(row=0, column=1)
        
        self.label_cellphone = tk.Label(self.root, text= 'Teléfono: ')
        self.label_cellphone.grid(row=1, column=0)
        self.entry_cellphone = tk.Entry(self.root)
        self.entry_cellphone.grid(row=1, column=1)
        
        self.register_client_btn = tk.Button(self.root, text='Registrar', command= self.register_client)
        self.register_client_btn.grid(row= 2, column= 0)
        
        self.root.mainloop()
    
    def register_client(self):
        name = self.entry_client.get()
        cellphone = self.entry_cellphone.get()
        
        if not self.controller_client.register_client(name, cellphone):
            messagebox.showerror('Error', 'El cliente ya existe')
        else:
            messagebox.showinfo('Exito', 'El cliente se ha registrado con éxito')