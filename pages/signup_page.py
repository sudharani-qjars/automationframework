from locators.signup_locators import SignUpLocators
from pages.base_page import BasePage

class SignUpPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def signup_address_info(self,first_name,last_name,company_name,address, address2,country
                            ,state, city, zip_code,mobile_number):
        self.enter_text(SignUpLocators.FIRST_NAME, first_name)
        self.enter_text(SignUpLocators.LAST_NAME, last_name)
        self.enter_text(SignUpLocators.COMPANY_NAME, company_name)
        self.enter_text(SignUpLocators.ADDRESS, address)
        self.enter_text(SignUpLocators.ADDRESS2, address2)
        self.select_dropdown(SignUpLocators.COUNTRY, country)
        self.enter_text(SignUpLocators.STATE, state)
        self.enter_text(SignUpLocators.CITY, city)
        self.enter_text(SignUpLocators.ZIP_CODE, zip_code)
        self.enter_text(SignUpLocators.MOBILE_NUMBER, mobile_number)

    def signup_title_password_dob(self, title, password, day, month, year):
        #self.scroll_into_view(SignUpLocators.TITLE,15000)
        self.click(SignUpLocators.TITLE)
        self.set_password(password)
        self.set_dob(day, month, year)
        # Call the base page methods

    def create_account(self):
        # add the create account button
        self.click(SignUpLocators.CREATE_ACCOUNT)

    def is_account_info_exists(self):
        return self.is_visible(SignUpLocators.LABEL_ACCOUNT_INFO)

    def set_password(self,password):
        self.enter_text(SignUpLocators.PASSWORD, password)

    def set_dob(self, day, month, year):
        self.select_dropdown(SignUpLocators.DAYS, day)
        self.select_dropdown(SignUpLocators.MONTHS, month)
        self.select_dropdown(SignUpLocators.YEARS, year)

