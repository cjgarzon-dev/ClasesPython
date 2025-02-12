# Patrón de diseño Factory

from abc import ABC, abstractmethod

# Clase abstarcta -> SuperClase
class Classes(ABC):
    
    @abstractmethod
    def operation(self):
        pass

# Creación de subclases
class ClassA(Classes):
    
    def operation(self):
        return 'Esta es la Clase A'

class ClassB(Classes):
    
    def operation(self):
        return 'Esta es la Clase B'

# Clase Factory
class FactoryClass:
    
    @staticmethod
    def creationObject(typeObject):
         if typeObject == 'A':
             return ClassA()
         elif typeObject == 'B':
             return ClassB()
         else:
             raise ValueError(f'La Clase {typeObject} no existe')
         
#object1 = FactoryClass.creationObject('A')
object2 = FactoryClass.creationObject('B')

#print(object1.operation())
print(object2.operation())