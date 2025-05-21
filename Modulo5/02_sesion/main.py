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

