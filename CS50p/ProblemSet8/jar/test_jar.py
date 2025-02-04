from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert(jar.capacity) == 12

def test_str():
    jar = Jar()
    jar.deposit(5)
    assert(str(jar)) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(15)
    jar.deposit(3)
    assert(jar.size) == 3

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(2)
    assert(jar.size) == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)
