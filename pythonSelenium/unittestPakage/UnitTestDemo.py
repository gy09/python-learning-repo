import unittest


class UnitTestDemoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        print(" I will run once before ")
    def setUp(self):
        print("I will run before every test case")

    def test_MethodA(self):
        print("Running Test Method A")

    def test_MethodB(self):
        print("Running test Method B")

    def tearDown(self):
        print("I will run after every test case ")

    @classmethod
    def tearDownClass(cls):

        print("I will run once after ")


if __name__ == '__main__':
    unittest.main(verbosity=2)
