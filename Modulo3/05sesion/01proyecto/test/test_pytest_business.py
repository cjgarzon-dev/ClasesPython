import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from business import SellerBase, SellerPremium

import pytest

def test_calculate_comission_base():
    seller = SellerBase('Pedro', 1000)
    assert seller.calculateComission() == 100.0
    
def test_calculate_comission_premium():
    seller = SellerPremium('Carlos', 2000)
    assert seller.calculateComission() == 300

if __name__ == '__main__':
    pytest.main()