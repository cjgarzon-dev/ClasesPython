import threading
from abc import ABC, abstractmethod

# Patrón sinlgeton
class SystemBilling:
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        
        if not cls._instance:
            cls._instance = super(SystemBilling, cls).__new__(cls)
            cls._instance._startHistorical()
        return cls._instance
        
        #opcional 
        '''
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(SystemBilling, cls).__new__(cls)
                cls._instance._startHistorical()
            return cls._instance
        '''
    def _startHistorical(self):
        self.historical = []
        print('Sistema de facturación inicializado')
        
    def registerOperation(self, operation):
        self.historical.append(operation)
        print(f'La operación fue registrada {operation}')
    
# Clase abstracta
class ProcessBusiness(ABC):
    
    @abstractmethod
    def ejecute(self):
        pass
    
class ProcessOrdering(ProcessBusiness):
    
    def ejecute(self):
        print('Procesando pedido...')
        return 'Pedido Procesado'
    
class ProcessBill(ProcessBusiness):
    
    def ejecute(self):
        print('Procesando factura...')
        return 'Factura Procesada'

# Crear la fabrica (patron Factory)
class FactoryProcessBusiness:
    
    @staticmethod
    def createProcess(typeProcess):
        if typeProcess == 'pedido':
            return ProcessOrdering()
        elif typeProcess == 'factura':
            return ProcessBill()
        else:
            raise ValueError(f'El proceso {typeProcess} no existe')

if __name__ == '__main__':
    
    system_Billing = SystemBilling()
    
    process1 = FactoryProcessBusiness.createProcess('pedido')
    process2 = FactoryProcessBusiness.createProcess('factura')
    
    resultOrdering1 = process1.ejecute()
    system_Billing.registerOperation(resultOrdering1)
    
    resultOrdering2 = process2.ejecute()
    system_Billing.registerOperation(resultOrdering2)
    
    print('\nHistorico de procesos de negocios')
    for operation in system_Billing.historical:
        print(f'Transacción: {operation}')