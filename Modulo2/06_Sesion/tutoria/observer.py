class NewChannel:
    def __init__(self):
        self._subscriber = []
        self._latersNews = None
    
    def subscribe(self, subscriber):
        self._subscriber.append(subscriber)
        
    def desubscriber(self, subscriber):
        self._subscriber.remove(subscriber)
        
    def notification(self):
        for subs in self._subscriber:
            subs.update(self._latersNews)
            
    def publication(self, news):
        self._latersNews = news
        print(f'Notificacion publicada: {news}')
        self.notification()
    
class Subscribers:
    def __init__(self, name):
        self.name = name
    
    def update(self, news):
        print(f'{self.name} ha recibido la notificacion: {news}')
        
canalDevSenior = NewChannel()

subs1 = Subscribers('Juan')
subs2 = Subscribers('Maria')
subs3 = Subscribers('Pedro')

canalDevSenior.subscribe(subs1)
canalDevSenior.subscribe(subs2)

canalDevSenior.publication('Tenemos tutoria el día de hoy')

canalDevSenior.subscribe(subs3)

canalDevSenior.publication('Tenemos 2 tutoría hoy')

canalDevSenior.desubscriber(subs2)

canalDevSenior.publication('Prueba 3')

    