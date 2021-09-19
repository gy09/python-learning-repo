import pytest


@pytest.mark.run(order=1)
def test_methodAA(OnetimesetUP, setUp):
    a = False
    assert a is False


@pytest.mark.run(order=3)
def test_methodBB(OnetimesetUP, setUp):
    a = False
    assert a is False


@pytest.mark.run(order=2)
def test_methodCC(OnetimesetUP, setUp):
    a = False
    assert a is False


@pytest.mark.run(order=5)
def test_methodDD(OnetimesetUP, setUp):
    a = False
    assert a is False


@pytest.mark.run(order=4)
def test_methodEE(OnetimesetUP, setUp):
    a = False
    assert a is False
