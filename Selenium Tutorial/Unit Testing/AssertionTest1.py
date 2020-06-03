from selenium import webdriver
import unittest


class testcase1(unittest.TestCase):
    def setUp(self):
        #print("testing")
        self.driver = webdriver.Chrome("C:/Users/dipta/Desktop/Tutorial/Selenium Tutorial/chromedriver.exe")
        self.driver.get("https://rifinder.com/")

        #This is assertIsNone and assertIsNotNone
        #self.assertIsNotNone(self.driver)
    

    #This is AssertTrue and assertFalse
    def not_test_Assertion(self):
        #Home - RiFinder
        title = self.driver.title
        self.assertFalse(title != "Home - RiFinder")

    #This is assertEqual and assertNotEqual
    def not_test_Assertion2(self):
        title = self.driver.title
        #self.assertEquals("Home - RiFinder Coding Site", title, "The title is not matched")
        self.assertNotEquals("Home - RiFinder", title)

    #This is assertGreater and asserLesser
    def test_Assertion3(self):
        self.assertGreater(100,10)
        self.assertGreaterEqual(100,100)
        self.assertLess(10,30)
        self.assertLessEqual()

        #self.assert

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()