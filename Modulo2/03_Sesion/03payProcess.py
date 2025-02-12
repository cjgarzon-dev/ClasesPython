# INTERFACES EN PYTHON

from abc import ABC, abstractmethod

class PayProcess(ABC):
    
    @abstractmethod        
    def payProcess(self, cant:float) -> None:
        pass
    
    @abstractmethod
    def payRefund(self, transactionId:str) -> None:
        pass
    
class Paypal(PayProcess):
    
    def payProcess(self, cant:float) -> None:
        print(f'Procesando pago de ${cant} por Paypal')
        
    def payRefund(self, transactionId:str) -> None:
        print(f'Reembolsando id transacción número: {transactionId} por Paypal')

class Stripe(PayProcess):
    
    def payProcess(self, cant:float) -> None:
        print(f'Procesando pago de ${cant} por Stripe')
        
    def payRefund(self, transactionId:str) -> None:
        print(f'Reembolsando id transacción número: {transactionId} por Stripe')
        
if __name__ == '__main__':
    paypalProcess = Paypal()
    stripeProcess = Stripe()
    
    paypalProcess.payProcess(500.0)
    paypalProcess.payRefund('123ABC')
    
    stripeProcess.payProcess(250.0)
    stripeProcess.payRefund('XYZ789')
    