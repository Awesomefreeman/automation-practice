from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        return self.driver.get(url)

    def hover_to_element(self, driver, locator):
        return ActionChains(driver).move_to_element(to_element=locator)

    def switch_to_iframe(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(locator))

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def wait_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def select(self, select_locator, index):
        select = self.find_element(select_locator)
        self.driver.execute_script(f"arguments[0].selectedIndex = {index}; arguments[0].dispatchEvent(new Event('change'))", select)
