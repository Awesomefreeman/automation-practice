from pytest_bdd import scenario, given, when, then
from pages.login_page import LoginPage
from pages.account_creation_page import AccountCreationPage


@scenario("register_scenario.feature", "Register on site")
def test_register():
    pass


@given("open authentication page")
def launch_browser(browser):
    LoginPage(browser).open()


@when("create new account")
def create_account(browser):
    LoginPage(browser).create_an_account()


@when("enter personal information")
def enter_info(browser):
    AccountCreationPage(browser).enter_personal_info()


@when("enter address")
def enter_address(browser):
    AccountCreationPage(browser).enter_address_info().submit_registration()


@then("register successful")
def check_register(browser):
    assert AccountCreationPage(browser).check_registration_complete()


