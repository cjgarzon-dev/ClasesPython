from view.menu import menu_principal
from config.database import DatabaseConexion

if __name__ == "__main__":
    db = DatabaseConexion()
    try:
        menu_principal(db)
    finally:
        db.cerrar_conexion()