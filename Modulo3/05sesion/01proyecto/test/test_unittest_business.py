import sys          #DEFINIRI Y CAPTURAR LA RUTA DONDE ESTA LA LOGICA DEL NEGOCIO
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from business import SellerBase, SellerPremium
import unittest

class TestSeller(unittest.TestCase):
    
    def setUp(self):
        self.sellerBase = SellerBase('Luis', 1000)          #COMISION = 100.0
        self.sellerPremium = SellerPremium('Pepe', 2000)    #COMISION = 300.0
    
    def test_calculate_comission_base(self):
        self.assertEqual(self.sellerBase.calculateComission(), 100.0)

    def test_calculate_comission_premium(self):
        self.assertEqual(self.sellerPremium.calculateComission(), 300.0)

if __name__ == '__main__':
    unittest.main()             # EJECUTAR EN LA TERMINAL: python -m unittest discover -s test