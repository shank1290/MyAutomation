from selenium.webdriver.common.by import By
from base.page_base import pageBase
class LoginPage(pageBase):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _link_Login_css = "[href='/sign_in']"
    _textbox_email_css = "input[type='email']"
    _textbox_password_css = "#user_password"
    _button_login_css = "input[type='submit']"
    _icon_userImage_css ="img.gravatar"
    _text_invalidlogin_csss = ".alert.alert-danger"

    def clickloginlink(self):
        self.clickElement(self._link_Login_css)
    def enteremail(self,email):
        self.sendkeys(email,self._textbox_email_css)
    def enterpassword(self,password):
        self.sendkeys(password, self._textbox_password_css)
    def clickloginbutton(self):
        self.clickElement(self._button_login_css)

    def login(self, email ="", password = ""):
       self.clickloginlink()
       self.clearTextField(self._textbox_email_css)
       self.enteremail(email)
       self.clearTextField(self._textbox_password_css)
       self.enterpassword(password)
       self.clickloginbutton()

    def isLoginSuccessful(self):
        result = self.isElementPresent(self._icon_userImage_css)
        return result

    def isLoginfailed(self):
        result = False
        msg = self.getTextFromElement(self._text_invalidlogin_csss)
        if msg in "Invalid email or password.":
            result = True
        return result

    def verifyTitle(self):
        print("------------------"+self.getTitle())
        if "Let's Kode It" in self.getTitle():
            return True
        else:
            return False




