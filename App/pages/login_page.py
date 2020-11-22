from pages.base import Base
from selenium.webdriver.common.by import By
import uuid


class Locators:
    login_locator = (By.CSS_SELECTOR, "input#email")
    password_locator = (By.CSS_SELECTOR, "input#passwd")
    submit_locator = (By.CSS_SELECTOR, "button#SubmitLogin")
    sign_out_locator = (By.CSS_SELECTOR, "a.logout")
    email_address_locator = (By.CSS_SELECTOR, "input#email_create")
    submit_create_locator = (By.CSS_SELECTOR, "button#SubmitCreate")


class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_url = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
        self.login = "cemeena@gmail.com"
        self.password = "C4!@TMR2n6L8a8U"

    def open(self):
        self.get(self.login_url)
        return self

    def enter_credentials(self):
        self.find_element(Locators.login_locator).send_keys(self.login)
        self.find_element(Locators.password_locator).send_keys(self.password)
        return self

    def submit(self):
        return self.find_element(Locators.submit_locator).click()

    def create_an_account(self):
        self.find_element(Locators.email_address_locator).send_keys("test" + str(uuid.uuid4()) + "@gmail.com")
        self.find_element(Locators.submit_create_locator).click()

    def check_sign_out_button(self):
        return self.find_element(Locators.sign_out_locator)

