from fuel import convert, gauge
import pytest

def test_str_convert():
    with pytest.raises(ValueError):
        convert("cat/dog")
def test_float_convert():
    with pytest.raises(ValueError):
        convert("5/7.5")
def test_xy_convert():
    with pytest.raises(ValueError):
        convert("5/4")
def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_gauge():
    assert(gauge(99)) == 'F'
    assert(gauge(100)) == 'F'
    assert(gauge(1)) == 'E'
    assert(gauge(0)) == 'E'

def test_gauge_percentage():
    assert(gauge(89)) == '89%'
    assert(gauge(15)) == '15%'
    assert(gauge(61)) == '61%'
    assert(gauge(40)) == '40%'
