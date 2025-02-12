## Clase Patrones de diseño avanzados (Observer y Strategy)

from abc import ABC, abstractmethod

class Subject:
    def __init__(self):
        self._observers = []
    
    def addObserver(self, observer):
        self._observers.append(observer)
        
    def removeObserver(self, observer):
        self._observers.remove(observer)
        
    def notificationObserver(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def update(self, message):
        raise NotImplementedError("Subclases deben estar implementadas")
    
class ObserverConcrete(Observer):
    
    def __init__(self, name):
        self.name = name 
    
    def update(self, message):
        print(f'{self.name} recibió: {message}')
    
subject = Subject()

obs1 = ObserverConcrete('Observador 1')
obs2 = ObserverConcrete('Observador 2')

subject.addObserver(obs1)
subject.addObserver(obs2)

subject.notificationObserver('Mensaje de advertencia LPTx')
