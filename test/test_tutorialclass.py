import time
import numpy as np
import pytest
try:
    from src.tutorialclass import Tutorialclass  # From PATH import function/class name
except:
    pass

def test_class():
    '''
    This tests whether the class fires up.
    '''
    test_numbers = [2,7,8]

    t = Tutorialclass()
    for x in test_numbers:
        t.add_number(x)
    cc = t.return_sum()

    assert type(cc) == dict
    assert cc['sum'] == np.sum(test_numbers)

def test_class_longlist():
    '''
    This tests whether the class fires up.
    '''
    test_numbers = np.random.randn(1000000)

    t_start = time.time()

    t = Tutorialclass()
    for x in test_numbers:
        t.add_number(x)
    cc = t.return_sum()

    t_end = time.time()
    print(t_end - t_start)

    assert cc['sum'] == np.sum(test_numbers)
    assert (t_end - t_start) < 1



