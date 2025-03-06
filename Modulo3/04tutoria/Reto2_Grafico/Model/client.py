class Client:
    def __init__(self, name, cellphone):
        self.name = name
        self.cellphone = cellphone
        self.pets = {}
        self.dates = {}
        
    def add_pet(self, pet):
        self.pets[pet.name] = pet
    
    def add_date(self, pet, date):
        if pet.name not in self.dates:
            self.dates[pet.name] = []
        self.dates[pet.name].append(date)
        