from config.database import DatabaseConexion
from models.estudiantes import Estudiante

class EstudianteControl:

    def __init__(self, db):
        self.db = db

    def registrar_estudiante(self, nombre, apellido, correo_electronico, telefono):
        sql = """
            INSERT INTO Estudiantes (nombre, apellido, correo_electronico, telefono) 
            VALUES (%s, %s, %s, %s)
        """
        parametros = (nombre, apellido, correo_electronico, telefono)
        self.db.execute_sql(sql, parametros)

    def listar_estudiantes(self):
        sql = """
            SELECT id_estudiante, nombre, apellido, correo_electronico, telefono FROM Estudiantes
        """
        resultados = self.db.execute_select(sql)
        return [Estudiante(*resultado) for resultado in resultados]
        