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
    '''Muestra el mensaje basado en el texto ingresado'''
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
app.geometry('700x800')
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

# Crear un frame para los botones de demostración
frame_buttons = ttk.LabelFrame(frame_principal, text='Estilo de Botones', padding=10)
frame_buttons.pack(fill=X, pady=20)

# Añadir botones con diferentes estilos
styles = ['primary', 'secondary', 'success', 'danger', 'warning', 'info']
for style in styles:
    ttk.Button(frame_buttons, text=style.capitalize(), bootstyle=style).pack(side=LEFT, padx=5, pady=10)

# Crear un frame para los controles
frame_controls = ttk.LabelFrame(frame_principal, text='Otros Controles', padding=10)
frame_controls.pack(fill=X, pady=10)

# Añadir una barra de progreso
progress = ttk.Progressbar(frame_controls, bootstyle='success-striped', value=75)
progress.pack(fill=X, pady=10)

# Añadir un control deslizante
ttk.Scale(frame_controls, from_=0, to=100, value=75, command=lambda val: progress.config(value=float(val))).pack(fill=X, pady=10)

# Añadir casillas de verificación
frame_check = ttk.Frame(frame_controls)
frame_check.pack(fill=X, pady=10)

for i, text in enumerate(['Opción 1', 'Opción 2', 'Opción 3']):
    ttk.Checkbutton(frame_check, text=text, bootstyle=styles[i % len(style)]).pack(side=LEFT, padx=10)

# Añadir un pie de página
footer = ttk.Label(app, text='TTK Boostrap - Interfaces modernas para Python', bootstyle='inverse-secondary')
footer.pack(side=BOTTOM, fill=X, pady=5)

app.mainloop()