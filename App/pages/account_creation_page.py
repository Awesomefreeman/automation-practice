from selenium.webdriver.common.by import By
from pages.base import Base


class Locators:
    gender_locator = (By.CSS_SELECTOR, "input#id_gender1")
    customer_firstname_locator = (By.CSS_SELECTOR, "input#customer_firstname")
    customer_lastname_locator = (By.CSS_SELECTOR, "input#customer_lastname")
    password_locator = (By.CSS_SELECTOR, "input#passwd")
    birth_day_locator = (By.CSS_SELECTOR, "select#days")
    birth_month_locator = (By.CSS_SELECTOR, "select#months")
    birth_year_locator = (By.CSS_SELECTOR, "select#years")
    firstname_locator = (By.CSS_SELECTOR, "input#firstname")
    lastname_locator = (By.CSS_SELECTOR, "input#lastname")
    company_name_locator = (By.CSS_SELECTOR, "input#company")
    address_locator = (By.CSS_SELECTOR, "input#address1")
    city_locator = (By.CSS_SELECTOR, "input#city")
    id_state_locator = (By.CSS_SELECTOR, "select#id_state")
    zip_code_locator = (By.CSS_SELECTOR, "input#postcode")
    mobile_phone_locator = (By.CSS_SELECTOR, "input#phone_mobile")
    submit_account_locator = (By.CSS_SELECTOR, "button#submitAccount")
    sign_out_locator = (By.CSS_SELECTOR, "a.logout")


class AccountCreationPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.firstname = "Test First Name"
        self.lastname = "Test Last Name"
        self.password = "testpassword4283572"
        self.company_name = "Test Company Inc."
        self.address = "64 King Dr. Cumming, GA 30040"
        self.city = "New York"
        self.zip_code = "10001"
        self.mobile_number = "+1 213 621 0002"

    def enter_personal_info(self):
        self.find_element(Locators.gender_locator).click()
        self.find_element(Locators.customer_firstname_locator).send_keys(self.firstname)
        self.find_element(Locators.customer_lastname_locator).send_keys(self.lastname)
        self.find_element(Locators.password_locator).send_keys(self.password)
        self.select(Locators.birth_day_locator, 1)
        self.select(Locators.birth_month_locator, 1)
        self.select(Locators.birth_year_locator, 20)
        return self

    def enter_address_info(self):
        self.find_element(Locators.firstname_locator).send_keys(self.firstname)
        self.find_element(Locators.lastname_locator).send_keys(self.lastname)
        self.find_element(Locators.company_name_locator).send_keys(self.company_name)
        self.find_element(Locators.address_locator).send_keys(self.address)
        self.find_element(Locators.city_locator).send_keys(self.city)
        self.select(Locators.id_state_locator, 1)
        self.find_element(Locators.zip_code_locator).send_keys(self.zip_code)
        self.find_element(Locators.mobile_phone_locator).send_keys(self.mobile_number)
        return self

    def submit_registration(self):
        self.find_element(Locators.submit_account_locator).click()

    def check_registration_complete(self):
        return self.find_element(Locators.sign_out_locator)
