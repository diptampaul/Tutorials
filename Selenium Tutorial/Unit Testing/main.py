import unittest

from package1.login import Login
from package1.signup import SignUp

from Package2.payment1 import DebitCard
from Package2.payment2 import CreditCard


#To get all the Test Cases on a WebPage
test1 = unittest.TestLoader().loadTestsFromTestCase(Login)
test2 = unittest.TestLoader().loadTestsFromTestCase(SignUp)
test3 = unittest.TestLoader().loadTestsFromTestCase(DebitCard)
test4 = unittest.TestLoader().loadTestsFromTestCase(CreditCard)



#Test Suite
sanityTestSuite = unittest.TestSuite([test1, test4, test2])
unittest.TextTestRunner().run(sanityTestSuite)