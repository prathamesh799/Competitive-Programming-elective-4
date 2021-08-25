import os,sys
sys.path.append(os.getcwd())
from nthwithproperty309 import nthwithproperty309
import pytest


@pytest.mark.parametrize('x, result',[
	(309, 0),
	(418, 1),
	(462, 2),
	(474, 3),
	(575, 4),
	(635, 5),
	(662, 6),
	(2014, 100),
	(7813, 1000)
])

def test_nthwithproperty309(result, x):
    assert nthwithproperty309(result) == x
