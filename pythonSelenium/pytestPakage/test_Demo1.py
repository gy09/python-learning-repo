import pytest



def test_firstcase(OnetimesetUP,setUp):
    a = 10
    b = 10
    assert a == b


def test_secondcase(OnetimesetUP,setUp):
    a = 20
    b = 10
    assert a == b
