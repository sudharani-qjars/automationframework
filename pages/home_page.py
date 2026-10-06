from locators.home_locators import HomeLocators
from pages.base_page import BasePage

class HomePage(BasePage):
    def click_home_tab(self):
        self.click(HomeLocators.HOME_TAB)

    def click_signup_tab(self):
        self.click(HomeLocators.SIGNUP_TAB)