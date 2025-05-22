import sqlite3
import mysql.connector

# Clase para manejar la conexión a la base de datos
class ConexionSQLite:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conexion = sqlite3.connect(db_path)
        self.cursor = self.conexion.cursor()
        print("Conexión exitosa a la base de datos SQLite")

class ConexionMySQL:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
    
        # Aquí iría la lógica para conectarse a MySQL
        self.conexion = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )    
        self.cursor = self.conexion.cursor()
        if self.conexion.is_connected():
            # Verificar la conexión
            print("Conexión exitosa a la base de datos MySQL")
        else:
            print("Error al conectar a la base de datos MySQL")
        
def main():
    # Crear una instancia de la clase ConexionSQLite
    db = ConexionSQLite('store_dev.db')
    
    # Ejecutar una consulta a la base de datos
    db.cursor.execute("SELECT * FROM teachers;")
    resultados = db.cursor.fetchall()
    
    # Imprimir los resultados
    for fila in resultados:
        print(fila)
    
    # Cerrar la conexión
    db.cursor.close()
    db.conexion.close()
    print("Conexión cerrada")

def main_mysql():
    # Crear una instancia de la clase ConexionMySQL
    db_mysql = ConexionMySQL(
        host="localhost",
        port=3306,
        user = "root",
        password = "admin",
        database = "store_dev"
    )
    
    # Ejecutar una consulta a la base de datos
    db_mysql.cursor.execute("SELECT * FROM clients;")   
    
    # Obtener los resultados
    resultados = db_mysql.cursor.fetchall()
    # Imprimir los resultados
    for fila in resultados:
        print(fila)
    
    # Cerrar la conexión   
    db_mysql.cursor.close()
    db_mysql.conexion.close()
    print("Conexión cerrada")

main()
main_mysql()