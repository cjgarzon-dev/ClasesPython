# Tutoria 18/12/2024
# https://refactoring.guru/es

import sqlite3

class DatabaseConnection:
    
    _instances = {}
    
    def __new__(cls, *args, **kwargs):
        if not cls._instances:
            cls._instances = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)
            cls._instances.connection = None
        return cls._instances
    
    def connect(self, dbName):
        if self.connection is None:
            self.connection = sqlite3.Connection(dbName)
            print('Conectado a la base de datos')
        else:
            print('Ya existe una conexión activa')
        return self.connection
    
    def closeConnection(self):
        if self.connection:
            self.connection.close()
            print('Conexión finalizada a la base de datos')
            self.connection = None
            
db1 = DatabaseConnection()
connection1 = db1.connect('my_db.db')

db2 = DatabaseConnection()
connection2 = db2.connect('my_db2.db')

db1.closeConnection()
db2.closeConnection()