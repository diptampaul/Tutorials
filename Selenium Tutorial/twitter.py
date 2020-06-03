from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import password


class TwitterBot:
    def __init__(self,email,password):
        self.username = email
        self.password = password
        self.driver = webdriver.Chrome("C:/Users/dipta/Desktop/Tutorial/Selenium Tutorial/chromedriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://twitter.com")
        sleep(5)

        user = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[1]/div/label/div/div[2]/div/input")
        user.clear()
        user.send_keys(self.username)

        passw = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[2]/div/label/div/div[2]/div/input")
        passw.clear()
        passw.send_keys((self.password))

        login = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[3]/div")
        login.click()
        sleep(10)

    def likeTweet(self,searchfor):
        driver = self.driver
        searchBox = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
        searchBox.send_keys(searchfor)
        searchBox.send_keys(Keys.RETURN)
        sleep(10)

        for i in range(1,3):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(2)


        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        likes = driver.find_elements_by_xpath("//div[@data-testid='like']")
        for like in likes:
            like.click()
            sleep(3)





p = password.Password()

email = p.returnEmail()
password = p.returnPass()

rifinder = TwitterBot(email,password)
rifinder.login()
rifinder.likeTweet("selenium")