from pages.base import Base
from selenium.webdriver.common.by import By


class Locators:
    login_locator = (By.CSS_SELECTOR, "input#email")
    password_locator = (By.CSS_SELECTOR, "input#passwd")
    submit_locator = (By.CSS_SELECTOR, "button#SubmitLogin")
    sign_out_locator = (By.CSS_SELECTOR, "a.logout")


class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_url = "http://automationpractice.com/index.php?controller=authentication&back=my-account"

    def open(self):
        self.get(self.login_url)
        return self

    def enter_credentials(self, login, password="HzPpTuY3hRAybm@"):
        self.find_element(Locators.login_locator).send_keys(login)
        self.find_element(Locators.password_locator).send_keys(password)
        return self

    def submit(self):
        return self.find_element(Locators.submit_locator).click()

    def check_sign_out_button(self):
        return self.find_element(Locators.sign_out_locator)

