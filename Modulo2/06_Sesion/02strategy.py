from abc import ABC, abstractmethod

class StrategyDiscount(ABC):
    
    @abstractmethod
    def calculate(self, mount):
        pass
    
class WithoutDiscount(StrategyDiscount):
    def calculate(self, mount):
        return mount

class DiscountPorcent(StrategyDiscount):
    
    def __init__(self, porcent):
        self.porcent = porcent
    
    def calculate(self, mount):
        return mount - (mount * self.porcent / 100)

class DiscountFixed(StrategyDiscount):
    
    def __init__(self, mountDiscount):
        self.mountDiscount = mountDiscount
        
    def calculate(self, mount):
        return mount - self.mountDiscount
    
class Order:
    
    def __init__(self, mount, strategyDiscount: StrategyDiscount):
        self.mount = mount
        self.strategyDiscount = strategyDiscount
        
    def calculateTotal(self):
        return self.strategyDiscount.calculate(self.mount)

order1 = Order(1000, WithoutDiscount())
print(f'Total sin descuento: {order1.calculateTotal()}')

order2 = Order(1000, DiscountPorcent(50))
print(f'Total con 50% de descuento: {order2.calculateTotal()}')

order3 = Order(1000, DiscountFixed(100))
print(f'Total con descuento fijo de $100: {order3.calculateTotal()}')