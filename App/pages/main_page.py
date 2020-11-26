from pages.base import Base
from selenium.webdriver.common.by import By


class Locators:
    items_locator = (By.CSS_SELECTOR, "div.product-container")
    add_to_cart_locator = (By.CSS_SELECTOR, "p#add_to_cart button[name='Submit']")
    quick_view_button_locator = (By.CSS_SELECTOR, "a.quick-view")
    quick_view_iframe_locator = (By.CSS_SELECTOR, "iframe.fancybox-iframe")
    proceed_to_checkout_locator = (By.CSS_SELECTOR, "a[title='Proceed to checkout'")


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.main_url = "http://automationpractice.com/"

    def go_to_main_page(self):
        self.get(self.main_url)
        return self

    def quick_preview_first_item(self):
        first_element = self.find_elements(Locators.items_locator)[0]
        self.hover_to_element(self.driver, first_element).perform()
        self.find_element(Locators.quick_view_button_locator).click()
        self.switch_to_iframe(Locators.quick_view_iframe_locator)

    def add_first_item_to_cart(self):
        self.find_element(Locators.add_to_cart_locator).click()
        self.find_element(Locators.proceed_to_checkout_locator).click()



