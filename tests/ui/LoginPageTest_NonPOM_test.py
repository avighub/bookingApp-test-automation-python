from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_navigate_To_LoginPage_with_chrome_exe():
    driver = webdriver.Chrome(
        'C:\\Users\\Wildwolf\\PycharmProjects\\bookingApp-test-automation\\chromedriver.exe')  # Optional argument, if not specified will search path.
    driver.get("https://www.saucedemo.com/")
    sleep(1)
    driver.quit()


# Using webdrivermanager- Improved
def test_navigate_To_LoginPage_UsingWebDriverManager():
    driver = webdriver.Chrome(
        ChromeDriverManager().install())  # Install chrome driver exe as per browser version found in system
    driver.get("https://www.saucedemo.com/")
    sleep(1)
    driver.quit()


# Selenium 4 update : WebDriver init using Service
def test_navigate_To_LoginPage_UsingWebDriverManagerService():
    # Preparation
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)  # Install chrome driver exe as per browser version found in system
    driver.get("https://www.saucedemo.com/")
    sleep(1)

    # execution
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    sleep(1)
    driver.find_element(By.ID, "login-button").click()
    sleep(1)

    # Assertion
    productTitleTxt = driver.find_element(By.CSS_SELECTOR,
                                          "#header_container > div.header_secondary_container > span").text
    assert productTitleTxt == "PRODUCTS"
    # tearDown or cleanUp
    driver.quit()
