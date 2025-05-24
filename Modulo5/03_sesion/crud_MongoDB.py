# Conexión con la base de datos
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

uri = "mongodb+srv://admin:admin@cluster0.wplig2p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Elegir una base de datos y colección
db = client['mi_base_de_datos']
collection = db['users']

# Crear un usuario
def create_user(name, age, email, city):
    """
    Crea un nuevo usuario en la base de datos.
    :param user_data: Diccionario con los datos del usuario.
    :return: ID del nuevo usuario creado.
    """
    collection.insert_one({'name': name, 'age': age, 'email': email, 'city': city})
    print(f"Usuario {name} creado con éxito.")

# Mostrar todos los usuarios
def show_users():
    """
    Muestra todos los usuarios en la base de datos.
    """
    users = collection.find()
    for user in users:
        print(user) 

# Actualizar un usuario
def update_user(user_id, new_name, new_age, new_email, new_city):
    """
    Actualiza un usuario en la base de datos.
    :param user_id: ID del usuario a actualizar.
    :param new_user_data: Diccionario con los nuevos datos del usuario.
    """
    #Se crea un nuevo diccionario con los nuevos datos
    new_Data = {}
    if new_name: new_Data['name'] = new_name
    if new_age: new_Data['age'] = new_age  
    if new_email: new_Data['email'] = new_email
    if new_city: new_Data['city'] = new_city
    
    if not new_Data:
        print("No se han proporcionado nuevos datos para actualizar.")
        return
    # Se actualiza el usuario en la base de datos
    result = collection.update_one(
        {'_id': ObjectId(user_id)},
        {'$set': new_Data}
    )
    if result.modified_count > 0:
        print(f"Usuario con ID {user_id} actualizado con éxito.")
    else:
        print(f"No se encontró un usuario con ID {user_id} o no se realizaron cambios.")

# Eliminar un usuario
def delete_user(user_id):
    """
    Elimina un usuario de la base de datos.
    :param user_id: ID del usuario a eliminar.
    """
    result = collection.delete_one({'_id': ObjectId(user_id)})
    if result.deleted_count > 0:
        print(f"Usuario con ID {user_id} eliminado con éxito.")
    else:
        print(f"No se encontró un usuario con ID {user_id}.")

# Consulta de usuario por Ciudad
def find_user_city(city):
    """
    Encuentra usuarios por ciudad.
    :param city: Ciudad a buscar.
    """
    for user in collection.find({'city': city}):
        if user:
            print(user)
        else:
            print(f"No se encontraron usuarios en la ciudad {city}.")

# Consulta de usuario por ciudad y edad
def find_user_city_age(city, age):
    resultado = collection.find(
        {'$and':[
            {'city': city},
            {'age': age}
        ]}
    )
    for user in resultado:
        if user:
            print('Ingresa IF')
            print(user)
            
        else:
            print('Ingresa ELSE')
            print(f"No se encontraron usuarios en la ciudad {city} con edad {age}.")

# Consulta de usuario por rango de edad
def find_user_age_range():
    result = collection.find({
        'age': {'$gte':18, '$lte':25}
    })
    for user in result:
        if user:
            print(user)
        else:
            print('No se encontraron usuarios en el rango de edad especificado.')

# Consulta por dos condiciones (entre dos ciudades)
def find_user_city_or(city1, city2):
    result = collection.find({
        '$or': [
            {'city': city1},
            {'city': city2}
        ]
    })
    for user in result:
        if user:
            print(user)
        else:
            print(f"No se encontraron usuarios en las ciudades {city1} o {city2}.")


# Crear un usuario nuevo
#create_user('Juan', 30, 'juan@example.com', 'Bogotá')

# Actualizar un usuario existente
print('\nActualizar un usuario existente')
update_user('6832460d5f1c01f678b89953', 'Pedro', 30, 'pedro@example.com', 'Cali')

# Eliminar un usuario
print('\nEliminar un usuario')
delete_user('683246c09ab865afc99fa99d')

# Mostrar todos los usuarios
# print('\nMostrar todos los usuarios')
#show_users()

# Consulta de usuario por ciudad
print('\nConsulta de usuario por ciudad')
find_user_city('Bogotá')

# Consulta de usuario por ciudad y edad
print('\nConsulta de usuario por ciudad y edad')
find_user_city_age('Bogotá', 30)

# Consulta de usuario por rango de edad
print('\nConsulta de usuario por rango de edad')
find_user_age_range()

# Consulta por dos condiciones (entre dos ciudades)
print('\nConsulta por dos condiciones (entre dos ciudades)')
find_user_city_or('Barranquilla', 'Bogotá')