from abc import ABC, abstractmethod
from tkinter import ttk, messagebox
import tkinter as tk
import datetime

# Variable global
clientes = []   
pets = []

# Clases Principales
class Veterinary:
    class Person:
        id_counter = 1
        
        def __init__(self, name, contact):
            self.name = name
            self.contact = contact
            
            self.id_counter = Veterinary.Person.id_counter
            Veterinary.Person.id_counter += 1

    class Client(Person):
        def __init__(self, name, contact, address):
            super().__init__(name, contact)
            self.address = address
            self.pet = []
        
        def addPet(self, pet):
            self.pet.append(pet)

    class Pet:
        id_counter = 1
        def __init__(self, name, specie, race, age):
            self.name = name
            self.specie = specie
            self.race = race
            self.age = age
            self.historyClinic = []
            self.id_counter = Veterinary.Pet.id_counter
            Veterinary.Pet.id_counter += 1
            
        def addDate(self, date):
            self.historyClinic.append(date)
        
        def eraseDate(self, date):
            self.historyClinic.remove(date)
                
        def showHistory(self):
            return self.historyClinic 

    class Date:
        id_counter = 1
        
        def __init__(self, date, hour, service, veterinarian):
            self.date = date
            self.hour = hour
            self.service = service
            self.veterinarian = veterinarian
            
            self.id_counter = Veterinary.Date.id_counter
            Veterinary.Date.id_counter += 1
            
# Funciones del sistemas
def registerClient(name, contact, address):

    cliente = Veterinary.Client(name, contact, address)
    clientes.append(cliente)
    messagebox.showinfo('Registro', f'Cliente registrado con ID: {cliente.id_counter}')

def registerPet(idClient, namePet, specie, race, age): 
    
    client = next((c for c in clientes if c.id_counter == idClient), None)
    if not client:
        messagebox.showerror('Error', 'Cliente no encontrado')
        return
    
    pet = Veterinary.Pet(namePet, specie, race, age)
    pets.append(pet)
        
    client.addPet(pet)
    messagebox.showinfo('Registro', f'Mascota con ID: {pet.id_counter} agregada con éxito')   

def scheduleDate():
    print('CLIENTES REGISTRADOS:')
    
    if not clientes:
        print('\tNo existen clientes registrados')
        return
    if not pets:
        print('\tNo existen mascotas registradas')
        return
        
    for c in clientes:
        print(f'\t|ID: {c.id_counter},| Nombre: {c.name}|')          
    
    try:
        client_id = int(input('Ingrese el ID del cliente: '))
        client = next((c for c in clientes if c.id_counter == client_id), None)
        if not client:
            raise ValueError(f'\tNo existe cliente registrado con el ID {client_id}')
        
        if not client.pet:
            raise ValueError(f'El cliente {client.name} no tiene mascotas registradas')
            
        print(f'Mascotas del cliente {client.name}: ')
        for p in client.pet:
            print(f'\t|ID Mascota: {p.id_counter},| Nombre Mascota {p.name}|')
            
        pet_id = int(input('Ingrese el ID de la mascota para agendar cita: ').strip())
        pet = next((p for p in client.pet if p.id_counter == pet_id), None)
        if not pet:
            raise ValueError(f'\tNo existe mascota registrada con el ID: {pet_id} para el cliente {client.name}')
        
        date = input('Ingrese la fecha de la cita (DD-MM-YY): ').strip()
        while not validateDate(date):
            print('Fecha inválida, por favor ingresa la fecha en el formato correcto (ejm. 31-01-25): ')
            date = input('Ingrese la fecha de la cita (DD-MM-YY): ').strip()
        hour = input('Ingrese la hora de la cita (12:00): ').strip()
        while not validateHour(hour):
            print('Hora inválida, por favor agregar la hora en el formato correcto (ejm. 12:00) : ')
            hour = input('Ingrese la hora de la cita (12:00): ').strip()
        service = input('Ingrese el servicio deseado: ').strip()
        veterinarian = input('Ingrese el nombre del veterinario: ').strip()
        
        appointment = Veterinary.Date(date, hour, service, veterinarian)
        pet.addDate(appointment)
        print('Cita agregada con éxito')
    except ValueError as e:
        print(f'Error: {e}')


def consultHistory():
    print('CLIENTES REGISTRADOS:')
    
    if not clientes:
        print('\tNo existen clientes registrados')
        return
    if not pets:
        print('\tNo existen mascotas registradas')
        return
    
    for c in clientes:
        print(f'\t--ID Cliente: {c.id_counter},-- Nombre cliente: {c.name},-- Mascotas: ⤵️')
        if not c.pet:
            print('\t\tNo tiene mascotas registradas')
        for p in c.pet:
            print(f'\t\t|ID Mascota: {p.id_counter},| Nombre mascota: |{p.name}')
    
    print('CONSULTAR HISTORIAL')
    try:
        client_id = int(input('Ingrese el ID del cliente: ').strip())
        client = next((c for c in clientes if c.id_counter == client_id), None)
        if not client:
            raise ValueError(f'\tNo existe cliente registrado con el ID {client_id}')
            
        if not client.pet:
            raise ValueError(f'\tEl cliente {client.name} no tiene mascotas registradas')
        
        print(f'Mascotas del cliente {client.name}: ')
        for p in client.pet:
            print(f'\tMascota: Nombre: {p.name}, ID: {p.id_counter}')
            
        pet_id = int(input('Ingrese el id de la mascota para consultar su historial: ').strip())
        pet = next((p for p in client.pet if p.id_counter == pet_id), None)
        if not pet:
            raise ValueError(f'\tNo existe mascota registrada con el ID: {pet_id} para el cliente {client.name}')
        
        pet.showHistory()
    except ValueError as e:
        print(f'Error: {e}')

def updateDate():
    if not clientes:
        print('No se tienen clientes registrados')
        return
    if not pets:
        print('No se tienen mascotas registradas')
        return
    
    print('Clientes y mascotas registrados')
    for c in clientes:
        print(f'Id cliente: {c.id_counter}, Nombre: {c.name}, Mascotas:')
        if not c.pet:
            print('\tNo tiene mascotas registradas')
        for p in c.pet:
            print(f'\tId mascota: {p.id_counter}, Nombre mascota: {p.name}')
    
    try:
        id_client = int(input('Ingrese el id del Cliente que desea consultar: '))
        client = next((c for c in clientes if c.id_counter == id_client), None)
        if not client:
            raise ValueError('No se encontró cliente registrado con ese ID')
        if not client.pet:
            raise ValueError(f'El cliente {client.name} no tiene mascotas registradas')
        
        print(f'Mascotas del cliente {client.name}')
        for p in client.pet:
            print(f'\tId mascota: {p.id_counter}, Nombre mascota: {p.name}')
        id_Pet = int(input('Ingrese el id de la mascota que desea consultar: '))
        pet = next((p for p in client.pet if p.id_counter == id_Pet), None)
        if not pet:
            raise ValueError('No se encontro máscota con ese ID')
        
        if not pet.historyClinic:
            raise ValueError(f'\tLa máscota con id {pet.id_counter} no tiene historial registrado')
        
        print('Citas disponibles para actualizar')
        pet.showHistory()
        
        id_History = int(input('Ingrese el id de la cita actualizar: '))
        history = next((h for h in pet.historyClinic if h.id_counter == id_History), None)
        
        if not history:
            raise ValueError('\tNo se encontro historial clínico con ese ID')
        
        dateNew = pet.historyClinic[id_History-1]
        print(f'Cambiando los datos de la cita... {id_History}')
    
        newDate = input('Ingrese la nueva fecha de la cita (DD-MM-YY): ').strip()
        while not validateDate(newDate):
            print('Fecha inválida, por favor ingresa la fecha en el formato correcto (ejm. 31-01-25): ')
            newDate = input('Ingrese la nueva fecha de la cita (DD-MM-YY): ').strip()
        newHour = input('Ingrese la nueva hora de la cita (12:00): ').strip()
        while not validateHour(newHour):
            print('Hora inválida, por favor agregar la hora en el formato correcto (ejm. 12:00) : ')
            newHour = input('Ingrese la nueva hora de la cita (12:00): ').strip()
        newService = input('Ingrese el nuevo servicio deseado: ').strip()
        newVeterinarian = input('Ingrese el nombre del nuevo veterinario: ').strip()
        
        dateNew.date = newDate
        dateNew.hour = newHour
        dateNew.service = newService
        dateNew.veterinarian = newVeterinarian
        
        print('Cita actualizada con exito')
    except ValueError as e:
        print(f'Error: {e}')

def eraseDate():
    if not clientes:
        print('No se tienen clientes registrados')
        return
    if not pets:
        print('No se tienen mascotas registradas')
        return
    
    print('Clientes y mascotas registrados')
    for c in clientes:
        print(f'Id cliente: {c.id_counter}, Nombre: {c.name}, Mascotas:')
        if not c.pet:
            print('\tNo tiene mascotas registradas')
        for p in c.pet:
            print(f'\tId mascota: {p.id_counter}, Nombre mascota: {p.name}')
    
    try:
        id_client = int(input('Ingrese el id del Cliente que desea consultar: '))
        client = next((c for c in clientes if c.id_counter == id_client), None)
        if not client:
            raise ValueError('No se encontró cliente registrado con ese ID')
        if not client.pet:
            raise ValueError(f'El cliente {client.name} no tiene mascotas registradas')
        
        print(f'Mascotas del cliente {client.name}')
        for p in client.pet:
            print(f'\tId mascota: {p.id_counter}, Nombre mascota: {p.name}')
        id_Pet = int(input('Ingrese el id de la mascota que desea consultar: '))
        pet = next((p for p in client.pet if p.id_counter == id_Pet), None)
        if not pet:
            raise ValueError('No se encontro máscota con ese ID')
        
        if not pet.historyClinic:
            raise ValueError(f'\tLa máscota con id {pet.id_counter} no tiene historial registrado')
        
        print('Citas disponibles para cancelar')
        pet.showHistory()
        
        id_History = int(input('Ingrese el id de la cita a cancelar: '))
        history = next((h for h in pet.historyClinic if h.id_counter == id_History), None)
        
        if not history:
            raise ValueError('\tNo se encontro historial clínico con ese ID')
        
        dateErase = pet.historyClinic[id_History-1]
        print(f'Cancelando la cita con id {id_History}')
        pet.eraseDate(dateErase)
        print('Cita cancelada con éxito')
    except ValueError as e:
        print(f'Error: {e}')
    

# Funciones auxiliares
def validateDate(date):
    from datetime import datetime
    try:
        datetime.strptime(date,'%d-%m-%y')
        return True
    except ValueError:
        return False

def validateHour(hour):
    from datetime import datetime
    try:
        datetime.strptime(hour, '%H:%M')
        return True
    except ValueError:
        return False
        

# Interface TKINTER
class VeterinaryGestion:
    def __init__(self, root):
        self.root = root
        self.root.title('Gestión de Veterinaria')
        self.root.geometry('500x500')
        
        self.clients = clientes
        self.pets = pets
        
        self.main_menu()
        
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text='Sistema de Veterinaria', font=('Arial', 16)).pack(pady=10)
        
        tk.Button(self.root, text='1. Registrar Cliente', command=self.registerClient).pack(pady=5)
        tk.Button(self.root, text='2. Registrar Mascota', command='').pack(pady=5)
        tk.Button(self.root, text='3. Registrar Cita', command='').pack(pady=5)
        tk.Button(self.root, text='4. Consultar historial mascota', command='').pack(pady=5)
        tk.Button(self.root, text='5. Actualizar cita', command='').pack(pady=5)
        
    def registerClient(self):
        self.clear_window()
        tk.Label(root, text='Registrar Cliente', font=('Arial', 14)).pack(pady=10)
        
        tk.Label(root, text='Nombre: ').pack(pady=5)
        name_entry = tk.Entry(self.root)
        name_entry.pack(pady=5)
        
        tk.Label(root, text='Contacto: ').pack(pady=5)
        contact_entry = tk.Entry(self.root)
        contact_entry.pack(pady=5)
        
        tk.Label(root, text='Dirección: ').pack(pady=5)
        address_entry = tk.Entry(self.root)
        address_entry.pack(pady=5)
        
        def submitClient():
            name = name_entry.get()
            contact = contact_entry.get()
            address = address_entry.get()
            self.registerPet()
            
            registerClient(name, contact, address)
        
        tk.Button(self.root, text='Registrar', command=submitClient).pack(pady=10)
        tk.Button(self.root, text='Menu principal', command=self.main_menu).pack(pady=10)
        
    def registerPet(self):
        self.clear_window()
        tk.Label(self.root, text='Registrar Mascota', font= ('Arial', 14)).pack(pady=10)
        
        tk.Label(self.root, text='Id Cliente: ').pack(pady=5)
        idClient_entry = tk.Entry(self.root)
        idClient_entry.pack(pady=5)
        
        tk.Label(self.root, text='Nombre: ').pack(pady=5)
        name_entry = tk.Entry(self.root)
        name_entry.pack(pady=5)
        
        tk.Label(self.root, text='Especie: ').pack(pady=5)
        specie_comboBox = ttk.Combobox(self.root, values=['Perro', 'Gato', 'Conejo', 'Ave', 'Otros'])
        specie_comboBox.pack(pady=5)
        
        tk.Label(self.root, text='Raza: ').pack(pady=5)
        race_entry = tk.Entry(self.root)
        race_entry.pack(pady=5)
        
        tk.Label(self.root, text='Edad: ').pack(pady=5)
        age_entry = tk.Entry(self.root)
        age_entry.pack(pady=5)
        
        def submit_pet():
            idClient = int(idClient_entry.get())
            name = name_entry.get()
            specie = specie_comboBox.get()
            race = race_entry.get()
            age = age_entry.get()
            self.main_menu()
            
            registerPet(idClient, name, specie, race, age)
            
        tk.Button(self.root, text='Registrar', command=submit_pet).pack(pady=10)
        tk.Button(self.root, text='Menu principal', command=self.main_menu).pack(pady=10)
        

root = tk.Tk()
app = VeterinaryGestion(root)
root.mainloop()
