from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
import utilities.custom_logger as cl
import logging

class pageBase:

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver


    def getElement(self, locator):
        element = None
        try:
            element = self.driver.find_element(By.CSS_SELECTOR,locator)
            self.log.info("element found")
        except:
            self.log.error("Element not found")
        return element

    def clickElement(self, locator):
        try:
            element = self.getElement(locator)
            element.click()
            self.log.info("Clicked on element with locator: " + locator )
        except:
            self.log.error("Cannot click on the element with locator: " + locator)
            print_stack()

    def sendkeys(self, data, locator):
        try:
            element = self.getElement(locator)
            element.send_keys(data)
            self.log.info("sent data on element with locator: " + locator )
        except:
            self.log.error("Cannot send data on the element with locator: " + locator)
            print_stack()

    def isElementPresent(self, locator):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.error("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def waitForElement(self, locator,timeout=10, pollFrequency=0.5):
        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            print_stack()
        return element

    def getTextFromElement(self, locator):
        try:
            result = self.getElement(locator).text
            self.log.info("Found Element with Locator :" + locator +" and text :" + result)
        except:
            self.log.error("Element not found with locator:"+locator)
        return result.strip()

    def clearTextField(self,locator):
        try:
            self.getElement(locator).clear()
            self.log.info("Cleared field with locator:"+ locator)
        except:
            self.log.error("Unable to find element with locator:"+ locator)

    def getTitle(self):
        return self.driver.title