import unittest

from unittestPakage.UnitTestDemo import UnitTestDemoTest
from unittestPakage.AssertMethod import AssertMethodTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(UnitTestDemoTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(AssertMethodTest)

Regression_Test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=5).run(Regression_Test)
