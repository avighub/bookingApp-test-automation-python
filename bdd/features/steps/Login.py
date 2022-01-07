from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())


@given(u'I navigate to swagLabs login page')
def step_impl(context):
    driver.get("https://www.saucedemo.com/")


@when(u'I enter "{uname}" and "{pwd}"')
def step_impl(context, uname, pwd):
    driver.find_element(By.ID, "user-name").send_keys(uname)
    driver.find_element(By.ID, "password").send_keys(pwd)
    sleep(1)
    driver.find_element(By.ID, "login-button").click()
    sleep(1)


@then(u'I should see Products Page')
def step_impl(context):
    productTitleTxt = driver.find_element(By.CSS_SELECTOR,
                                          "#header_container > div.header_secondary_container > span").text
    assert productTitleTxt == "PRODUCTS"


@then(u'I close the browser')
def step_impl(context):
    # tearDown or cleanUp
    driver.quit()
