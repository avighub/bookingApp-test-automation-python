from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# Using driver exe - Not so convinient way
def test_navigateToLoginPage():
    driver = webdriver.Chrome(
        'C:\\Users\\Wildwolf\\PycharmProjects\\bookingApp-test-automation\\chromedriver.exe')  # Optional argument, if not specified will search path.
    driver.get("https://www.saucedemo.com/")
    driver.quit()


def test_navifateToLoginUsingWebDriverManager():
    driver = webdriver.Chrome(
        ChromeDriverManager().install())  # Install chrome driver exe as per browser version found in system
    driver.get("https://www.saucedemo.com/")
    driver.quit()
