from abc import ABC, abstractmethod

class StrategyRates(ABC):
    
    @abstractmethod
    def calculateRate(self, distance, time):
        raise NotImplementedError('Se debe implementar este método')
    
class RateFixed(StrategyRates):
    def calculateRate(self, distance, time):
        return 300
    
class RateHour(StrategyRates):
    def calculateRate(self, distance, time):
        return time * 25
    
class RateKilometer(StrategyRates):
    def calculateRate(self, distance, time):
        return distance * 2

class CalculaterRate:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def changeStrategy(self, strategy):
        self.strategy = strategy
        
    def calculate(self, distance, time):
        return self.strategy.calculateRate(distance, time)

rent1 = RateFixed()
calculator = CalculaterRate(rent1)
print(f'La tarifa fija: {calculator.calculate(10,5)}')

calculator.changeStrategy(RateHour())
print(f'Tarifa por hora: {calculator.calculate(100,2)}')

calculator.changeStrategy(RateKilometer())
print(f'Tarifa por kilometro: {calculator.calculate(100,3)}')