from Model.veterinary import Veterinary

class Controller_Client:
    def __init__(self):
        self.veterinary = Veterinary
        
    def register_client(self, name, cellphone):
        return self.veterinary.register_client(name, cellphone)
    
    def get_client(self, name):
        return self.veterinary.clients[name]
    