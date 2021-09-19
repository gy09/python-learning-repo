import pytest
from pytestPakage.test_classDemo import Test_classDemo1


@pytest.mark.usefixtures("OnetimesetUP", "setUp")
class Test_classDemo2():

    @pytest.fixture(autouse=True)
    def classsetUp(self):
        self.demo = Test_classDemo1(10)

    def test_methodA1(self):
        result = self.demo.verifyAddition(10, 20)

        assert result == 40

    def test_methodB1(self):
        result = self.demo.verifyAddition(10, 20)
        assert result > 20
        print("This is a test method")
