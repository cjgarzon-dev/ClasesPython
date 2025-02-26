from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Seller(ABC):
    name : str
    sales : float
    
    @abstractmethod
    def calculateComission(self) -> float:
        pass

@dataclass
class SellerBase(Seller):
    def calculateComission(self) -> float:
        return self.sales * 0.10

@dataclass
class SellerPremium(Seller):
    def calculateComission(self) -> float:
        return self.sales * 0.15
    
    