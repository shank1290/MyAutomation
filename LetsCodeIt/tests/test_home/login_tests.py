from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
       self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("shashank.1290@gmail.com", "Test@123")
        result1 = self.lp.verifyTitle()
        assert result1 == True
        result2 = self.lp.isLoginSuccessful()
        assert result2 == True


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("shashank.1290@gmail.com", "Test@1234")
        result = self.lp.isLoginfailed()
        assert result == True
