import pytest


class Test_classDemo1:

    def __init__(self, value):
        self.value = value

    def verifyAddition(self, a, b):
        return a + b + self.value
