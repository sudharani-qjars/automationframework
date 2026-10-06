from locators.login_locators import LoginLocators
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def login(self, username, email_id):
        self.enter_text(LoginLocators.USERNAME, username)
        self.enter_text(LoginLocators.EMAIL_ID, email_id)
        self.click(LoginLocators.SIGNUP_BUTTON)
