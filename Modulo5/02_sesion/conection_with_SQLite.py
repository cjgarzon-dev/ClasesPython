# Se importa las librerias necesarias
import sqlite3

# Se crea la conexion a la base de datos
conexion = sqlite3.connect('store_dev.db')

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Insertar un nuevo registro
query = 'INSERT INTO teachers(name_teacher, specialty_teacher, experience_teacher) VALUES(?,?,?);'
values = ('Cristhian Garzón', 'Python', 5)
cursor.execute(query, values)
print(f'Fila insertada: {cursor.rowcount}')

conexion.commit() 

# Ejecutar una consulta a la base de datos
cursor.execute("SELECT * FROM teachers;")
resultados = cursor.fetchall()
print(type(resultados))

# Imprimir los resultados  
for fila in resultados:
    print(fila)

# Cerrar la conexión
cursor.close()
conexion.close()