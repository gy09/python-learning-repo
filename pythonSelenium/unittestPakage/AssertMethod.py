import unittest


class AssertMethodTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(" Running Once Before the assertion test suite")

    def setUp(self):
        print("Running once before every test case")

    def test_assert_method1(self):
        a = True
        self.assertTrue(a, msg='A is not True')

        b = False
        self.assertEqual(a, b, msg='A and B are not equal')

    def test_asser_method2(self):
        a = 10
        b = 20

        self.assertNotEqual(a, b, msg="A and B are equal")

    def tearDown(self):
        print("I will run once After every test case")

    @classmethod
    def tearDownClass(cls):
        print("I will run after every test suite")


if __name__ == '__main__':
    unittest.main(verbosity=3)
