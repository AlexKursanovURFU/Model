import numpy as np
from src.model.lotka_volterra import lotka_volterra

def test_lotka_volterra():
    y = lotka_volterra(0, [10, 5])
    assert len(y) == 2

 