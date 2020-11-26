from pytest_bdd import scenario, given, when, then, parsers
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


@scenario("shopping_scenario.feature", "Buying item")
def test_buy_item():
    pass


@given('open main page')
def open_main_page(browser):
    MainPage(browser).go_to_main_page()


@when('quick view first item')
def quick_view(browser):
    MainPage(browser).quick_preview_first_item()


@when('add item to cart')
def add_item_to_cart(browser):
    MainPage(browser).add_first_item_to_cart()


@when('proceed to checkout')
def proceed_to_checkout(browser):
    OrderPage(browser).proceed_to_checkout()
    LoginPage(browser).enter_credentials().submit()
    OrderPage(browser).proceed_to_checkout().agree_with_terms_of_service().\
        proceed_to_checkout().pay_by_bank_wire().confirm()


@then(parsers.parse('i should see "{text}"'))
def checkout_was_completely_successful(browser, text):
    assert text in OrderPage(browser).get_order_confirmation_text()
