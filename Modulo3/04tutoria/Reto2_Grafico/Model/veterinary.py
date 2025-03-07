from .client import Client
from .pet import Pet
from .date import Date

class Veterinary:
    def __init__(self):
        self.clients = {}
        
    def register_client(self, name, cellphone):
        print('ENTRA A FUNCIÓN')
        if name not in self.clients:
            self.clients[name] = Client(name, cellphone)
            print('ENTRA A IF')
            return True
        return False
    

# HACER LO MISMO PARA MASCOTA Y CITA