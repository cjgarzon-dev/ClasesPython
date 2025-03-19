import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Crear la ventana principal con un tema
app = ttk.Window(themename='darkly')
app.title('Mi Primera App con TTKBoostrap')
app.geometry('500x400')

# Añadir un título
tittle = ttk.Label(app, text='Bienvendido a TTKBoostrap', font=('Helvetica', 24))
tittle.pack(pady=20)

# Añadir un botón de estilo primario
button_primary = ttk.Button(app, text='Botón Principal', bootstyle= 'primary')
button_primary.pack(pady=10)

# Añadir un botón de estilo secundario
button_secondary = ttk.Button(app, text='Botón Principal', bootstyle= 'secondary')
button_secondary.pack(pady=10)

# Añadir campo de entrada
entry_field = ttk.Entry(app)
entry_field.pack(pady=10, padx=50, fill=X)

app.mainloop()