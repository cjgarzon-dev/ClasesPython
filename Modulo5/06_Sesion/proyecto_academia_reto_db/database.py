import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error, IntegrityError

# Cargar las variables de entorno desde el archivo .env
load_dotenv()