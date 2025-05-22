# Primera conexión a base de datos
# Importar librerías
import mysql.connector

# Configuracion para la conexión a la base de datos
conexion = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "admin",
    database= "store_dev",
    port= 3306
)

# Verificar la conexión
if conexion.is_connected():
    print("Conexión exitosa a la base de datos")
    
# Realizar una consulta a la base de datos
cursor = conexion.cursor()
cursor.execute("SELECT * FROM clients;")
# Obtener los resultados
resultados = cursor.fetchall()
print(type(resultados))

# Imprimir los resultados
for fila in resultados:
    print(fila)
'''
# Insertar un nuevo registro
query = "INSERT INTO clients(name_client, email_client, cellphone_client) VALUES(%s, %s, %s);"
values = ('Cristhian Garzón', 'cristhian.garzon@example.com', '3102834281')
cursor.execute(query, values)
'''

print(f'Fila insertada: {cursor.rowcount}')

# Actualizar un registro
query = "UPDATE clients SET cellphone_client = %s WHERE id_client = %s;"
valores = ('3102834283', 11)
cursor.execute(query, valores)

print(f'Fila actualizada: {cursor.rowcount}')

# Eliminar un registro
query = "DELETE FROM clients WHERE id_client = %s;"
valores = (13,)
cursor.execute(query, valores)

print(f'Fila eliminada: {cursor.rowcount}')

# Confirmar los cambios 
conexion.commit()

# Cerrar conexion
conexion.close()
print("...")
print("Conexión cerrada")




