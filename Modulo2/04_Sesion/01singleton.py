## Clase de Patrones de diseño básicos: Singleton y Factory
## 10/12/2024

# Patrón de diseño singleton
class SingletonCreateInstance:
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):               # La definición '__new__' identifica que es un patrón singleton
        
        if not cls._instance:
            cls._instance = super(SingletonCreateInstance, cls).__new__(cls)
            return cls._instance
    