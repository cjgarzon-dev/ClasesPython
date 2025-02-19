# CLASE GESTION AVANZADA DE ERRORES DE APLICACIONES _ 31/ENE/2025

## INTERFACE TKINTER -> ES UNA LIBRERIA QUE PERMITE HACER APLICACIONES A TRAVÉS DE INTERFACES
from tkinter import *
import tkinter as tk

def converter():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result.config(text=f'Resultado: {fahrenheit:.2f}°F')
    except:
        result.config(text='Ingrese un número válido')
    
# CONFIGURACION DE LA VENTANA
root = tk.Tk()
root.title('Conversor de Temperatura')      # TITULO DE CUADRO 
root.geometry('500x300')                    # TAMAÑO EN PIXELES

# WIDGETS
tk.Label(root, text='Ingrese temperatura en °C:').pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text='Convertir', command=converter).pack(pady=5)
result = tk.Label(root, text='Resultado: ')
result.pack(pady=5)

root.mainloop()