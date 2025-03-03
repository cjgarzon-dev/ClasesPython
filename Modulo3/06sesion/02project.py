import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)

@dataclass
class Seller:
    name : str
    sales_totales : float

    def calculateComission(self) -> float:
        if self.sales_totales > 10000:
            comission = self.sales_totales*0.1
            logging.debug(f'{self.name} ha alcanzado el umbral de ventas. La comisión calculada es de ${comission}')
        else:
            comission = self.sales_totales * 0.05
            logging.debug(f'{self.name} no ha alcanzado el umbral de ventas. La comisión calculada es de ${comission}')
        return comission

if __name__ == '__main__':
    seller1 = Seller('Peter', 12000)
    print(f'La comisión de {seller1.name}: {seller1.calculateComission()}')