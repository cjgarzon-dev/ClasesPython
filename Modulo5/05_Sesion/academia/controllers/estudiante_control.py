from config.database import DatabaseConexion

class EstudianteControl:

    def __init__(self, db):
        self.db = db

    def registrar_estudiante(self, nombre, apellido, correo_electronico, telefono):
        sql = """
            INSERT INTO Estudiantes (nombre, apellido, correo_electronico, telefono) 
            VALUES (%s, %s, %s, %s)
        """
        parametros = (nombre, apellido, correo_electronico, telefono)
        self.db.ejecutar_sql(sql, parametros)

        