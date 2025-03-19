import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def change_theme():
    '''Cambia el tema de la aplicación'''
    themes = ['darkly', 'solar', 'superhero', 'cosmo', 'flatly', 'litera']
    theme_actual = app.style.theme.name
    
    # Obtener el índice del tema actual y seleccionar el siguiente
    index_actual = themes.index(theme_actual) if theme_actual in themes else 0
    new_theme = themes[(index_actual + 1) % len(themes)]
    app.style.theme_use(new_theme)
    tag_theme_actual.config(text=f'Tema actual: {new_theme}')

def show_message():
    text = tag_entry.get()
    if not text:
        text = 'Hola TTKBoostrap'
    
    # Crear diálogo modal
    dialogue = ttk.Toplevel(app)
    dialogue.title('Mensaje')
    dialogue.geometry('300x150')
    
    # Centrar el diálogo en la ventana principal
    x = app.winfo_x() + (app.winfo_width() - 300) // 2
    y = app.winfo_y() + (app.winfo_height() - 150) // 2
    dialogue.geometry(f'+{x}+{y}')
    
    # Añadir contenido al dialogo
    ttk.Label(dialogue, text=text, font=('Helvetica', 12), wraplength=250).pack(expand=YES, fill=BOTH, padx=20, pady=20)
    
    # Boton para cerra el dialogo
    ttk.Button(dialogue, text='Cerrar', bootstyle='danger', command=dialogue.destroy).pack(pady=10)
    
    
app = ttk.Window(themename='darkly')
app.title('Demo Básica de TTKBoostrap')
app.geometry('600x500')
app.resizable(True, True)

# Crear un frame principal
frame_principal = ttk.Frame(app, padding=20)
frame_principal.pack(fill=BOTH, expand=YES)

# Añadir un título
tittle = ttk.Label(frame_principal, text='Bienvenido a TTKBoostrap', font=('Helvetica', 24), bootstyle='inverse-primary')
tittle.pack(pady=20)

# Añadir etiqueta para mostrar el tema actual
tag_theme_actual = ttk.Label(frame_principal, text='Tema actual: darkly', font=('Helvetica', 12))
tag_theme_actual.pack(pady=5)

# Añadir botón para cambiar el tema
button_theme = ttk.Button(frame_principal, text='Cambiar Tema', bootstyle='info', command=change_theme)
button_theme.pack(pady=10)

# Crear un separador
ttk.Separator(frame_principal).pack(fill=X, pady=20)

# Crear un frame de entrada
frame_entry = ttk.Frame(frame_principal)
frame_entry.pack(fill=X, pady=10)

# Añadir la etiqueta de entrada
ttk.Label(frame_entry, text='Escribe un mensaje: ', font=('Helvetica', 12)).pack(side=LEFT, padx=5)

# Añadir el campo de entrada:
tag_entry = ttk.Entry(frame_entry, width=30)
tag_entry.pack(side=LEFT, padx=5, fill=X, expand=YES)

# Añadir boton para mostrar mensaje al usuario
button_message = ttk.Button(frame_entry, text='Mostrar', bootstyle='success', command=show_message)
button_message.pack(side=LEFT, padx=5)

app.mainloop()