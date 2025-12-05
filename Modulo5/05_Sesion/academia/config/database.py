import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error, IntegrityError

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class DatabaseConexion:
    def __init__(self):
        self.conectar = mysql.connector.connect(
            host=os.getenv("DB_HOST"), 
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.conectar.cursor()

    def ejecutar_sql(self, sql, parametros=None):
        try:
            if parametros:
                self.cursor.execute(sql, parametros)
            else:
                self.cursor.execute(sql)
            self.conectar.commit()
        except IntegrityError as e:
           raise IntegrityError(f"Error de integridad: {e.msg}")
        except Error as e:
            raise Exception(f"Error al ejecutar SQL: {e.msg}")

    def cerrar_conexion(self):
        self.cursor.close()
        self.conectar.close()

