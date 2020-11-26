from pages.base import Base
from selenium.webdriver.common.by import By


class Locators:
    checkout_locator = (By.XPATH, "//p//span[contains(., 'Proceed to checkout')]")
    terms_of_service_locator = (By.CSS_SELECTOR, "input#cgv")
    pay_by_bank_wire_locator = (By.CSS_SELECTOR, "a.bankwire")
    confirm_locator = (By.XPATH, "//button/span[contains(., 'I confirm my order')]")
    order_complete_locator = (By.CSS_SELECTOR, "p strong")


class OrderPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.order_url = "http://automationpractice.com/index.php?controller=order"

    def open(self):
        self.get(self.order_url)
        return self

    def proceed_to_checkout(self):
        self.find_element(Locators.checkout_locator).click()
        return self

    def agree_with_terms_of_service(self):
        self.find_element(Locators.terms_of_service_locator).click()
        return self

    def pay_by_bank_wire(self):
        self.find_element(Locators.pay_by_bank_wire_locator).click()
        return self

    def confirm(self):
        self.find_element(Locators.confirm_locator).click()
        return self

    def get_order_confirmation_text(self):
        complete_text = self.find_element(Locators.order_complete_locator)
        return complete_text.text
