
from selenium import webdriver
class GetWebDriver():

    def __init__(self,browser):
        self.browser =  browser


    def getDriverInstance(self):
        baseURL = 'https://learn.letskodeit.com'
        if self.browser == "Chrome":
            driver = webdriver.Chrome(executable_path='C:\\Users\\shahsnak\\Downloads\\chromedriver.exe')
            print("Running Test on Chrome")
        elif self.browser == "FireFox":
            driver = webdriver.Firefox()
            print("Running Test on Chrome")
        else:
            driver = webdriver.Chrome(executable_path='C:\\Users\\shahsnak\\Downloads\\chromedriver.exe')
            print("Running Test on Chrome")
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        return driver

