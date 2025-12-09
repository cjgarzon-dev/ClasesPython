import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error, IntegrityError

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class DatabaseConexion:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"), 
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.connection.cursor()

    def execute_sql(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
        except IntegrityError as e:
           raise IntegrityError(f"Error de integridad: {e.msg}")
        except Error as e:
            raise Exception(f"Error al ejecutar SQL: {e.msg}")
    
    def execute_select(self, query, parametros=None):
        try:
            if parametros:
                self.cursor.execute(query, parametros)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            raise Exception(f"Error al ejecutar SQL: {e.msg}")
    
    def fetchone(self):
        return self.cursor.fetchone()

    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()

