import pytest
from my_basics import *


def test_addition():
    assert add(2, 3) == 5


def test_multiplication():
    assert multiply(3, 5) == 15
