from plates import is_valid

def test_length():
    assert(is_valid("AAAA222")) == False
    assert(is_valid("A")) == False
def test_begin():
    assert(is_valid("A22")) == False
def test_alnum():
    assert(is_valid("AA!2")) == False
def test_mid():
    assert(is_valid("A2A2")) == False
def test_firstno():
    assert(is_valid("AB05")) == False
