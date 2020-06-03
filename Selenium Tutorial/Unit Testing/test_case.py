from selenium import webdriver
import unittest


class testcase1(unittest.TestCase):
    def setUp(self):
        #print("testing")
        self.driver = webdriver.Chrome("C:/Users/dipta/Desktop/Tutorial/Selenium Tutorial/chromedriver.exe")
        self.driver.get("https://rifinder.com/")
    
    
    def test_First_Case(self):
        print("This is successful test case")

    @unittest.SkipTest
    def test_Second_Case(self):
        print("This is successful 2nd test case")

    @unittest.skip("This test case is not yet ready")
    def test_Third_Case(self):
        print("This is successful 3rd test case")

    @unittest.skipIf(10==10,"Numbers are not equal")
    def test_Fourth_Case(self):
        print("This is successful 4th test case")

    def not_Test_Case(self):
        print("This will not perform")

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()