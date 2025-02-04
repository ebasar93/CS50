from bank import value

def test_hello():
    assert(value('hello')) == 0
    assert(value('HELLO')) == 0
    assert(value('hello, David')) == 0
def test_h():
    assert(value('hey')) == 20
    assert(value('hi')) == 20
def test_no():
    assert(value('am')) == 100
    assert(value('David hello')) == 100

