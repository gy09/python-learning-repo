import pytest


def test_methodC(OnetimesetUP, setUp):
    a = True
    assert a is True


def test_methodD(OnetimesetUP, setUp):
    a = False
    assert a is False
