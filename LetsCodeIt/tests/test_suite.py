import unittest
from tests.test_home import login_tests


sm1 = unittest.TestLoader().loadTests(login_tests)

smokeTest = unittest.TestSuite(sm1)

unittest.TextTestRunner(verbosity=2).run(smokeTest)
