from base.drivers import  GetWebDriver
import logging
import utilities.custom_logger as cl

class TestStatus(GetWebDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.testList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.testList.append("PASS")
                    self.log.info("##### Test Passes"+ resultMessage)
                else:
                    self.testList.append("FAIL")
                    self.log.error("##### Test Failed"+ resultMessage)
            else:
                self.log.error("##### Result not Found"+ resultMessage)
        except:
            self.testList.append("FAIL")
            self.log.error("##### Execption Occured"+ resultMessage)

    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)
