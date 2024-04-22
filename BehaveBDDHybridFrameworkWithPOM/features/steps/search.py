from behave import *
from selenium.webdriver.common.by import By

from features.pages.HomePage import HomePage
from features.pages.SearchPage import SearchPage


@given('User is able to navigate to Home Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.get_title_of_page.__eq__("Your Store")


@when('User enters a valid Product say {product}')
def step_impl(context, product):
    context.home_page.enter_product_into_search_field(product)


@when('User clicks on Search button')
def step_impl(context):
    context.search_page = context.home_page.click_on_search_button()


@then(u'Valid products should get displayed in Search Page say {product}')
def step_impl(context, product):
    assert context.search_page.display_status_of_product(product)


@when('User enters a Invalid Product say {product}')
def step_impl(context, product):
    context.home_page.enter_product_into_search_field(product)


@then('InValid products message get displayed in Search Page')
def step_impl(context):
    assert context.search_page.display_message_displayed("There is no product that matches the search criteria.")


@when(u'User enters no Product say {product}')
def step_impl(context, product):
    context.home_page.enter_product_into_search_field(product)


@then('No products should get displayed in Search Page')
def step_impl(context):
    assert context.search_page.display_message_displayed("There is no product that matches the search criteria.")
