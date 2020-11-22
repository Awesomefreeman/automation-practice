from pytest_bdd import scenario, given, when, then
from pages.login_page import LoginPage


@scenario("login_scenario.feature", "Login on site")
def test():
    pass


@given("open authentication page")
def launch_browser(browser):
    LoginPage(browser)


@when("enter credentials and login")
def open_auth_page(browser):
    LoginPage(browser).open().enter_credentials("arkadybaldin@gmail.com").submit()


@then("verify that \"sign out\" button exist")
def verify_sign_out(browser):
    assert LoginPage(browser).check_sign_out_button()
