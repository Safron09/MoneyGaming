from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_JOIN = (By.XPATH, "//a [@href='/sign-up.shtml']")
FIRSTNAME = (By.NAME, 'map(firstName)')
LASTNAME = (By.NAME, 'map(lastName)')
TICKBOX = (By.NAME, "map(terms)")
JOINAGAIN = (By.XPATH, "//fieldset [@class = 'underlay']//input[@id = 'form']")
RESULTS = (By.XPATH, "//label [@for = 'dob'][text()='This field is required']")


@given('Open Moneygaming page')
def open_money(context):
    context.driver.get('https://moneygaming.qa.gameaccount.com/')

@when('Search for "Join Now" button and Click')
def join_now(context):
    context.driver.find_element(*SEARCH_JOIN)
    context.driver.find_element(*SEARCH_JOIN).click()

@when('Enter First Name')
def enter_firstname(context):
    search = context.driver.find_element(*FIRSTNAME)
    search.clear()
    search.send_keys("James")
    sleep(3)

@when('Enter {search_word}')
def enter_lastname(context, search_word):
    search = context.driver.find_element(*LASTNAME)
    search.clear()
    search.send_keys(search_word)
    sleep(3)

@then('Check tickbox')
def check_tickbox(context):
    context.driver.find_element(*TICKBOX)
    context.driver.find_element(*TICKBOX).click()

@then('Press "Join Now" button')
def press_join(context):
    context.driver.find_element(*JOINAGAIN)
    context.driver.find_element(*JOINAGAIN).click()


@then('Result contains {search_word}')
def verify_first_result(context, search_word):
    first_result = context.driver.find_element(*RESULTS).text
    print('\n{}'.format(first_result))
    assert search_word in first_result, "Expected word '{}' in message, but got '{}'".format(search_word, first_result)
