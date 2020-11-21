from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from pytest import fixture
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@scenario("login_scenario.feature", "Login on site")
def test():
    pass


@given("open authentication page")
def launch_browser(browser):
    browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")


@when("enter credentials and login")
def open_auth_page(browser):
    browser.find_element_by_css_selector("input#email").send_keys("arkadybaldin@gmail.com")
    browser.find_element_by_css_selector("input#passwd").send_keys("HzPpTuY3hRAybm@")
    browser.find_element_by_css_selector("button#SubmitLogin").click()


@then("verify that \"sign out\" button exist")
def verify_sign_out(browser):
    assert is_element_present(browser, By.CSS_SELECTOR, "a.logout") == True


def is_element_present(browser, *args):
    try:
        browser.find_element(*args)
        return True
    except NoSuchElementException:
        return False
