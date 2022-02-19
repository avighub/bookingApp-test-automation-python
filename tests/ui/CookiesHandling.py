from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

def test_navigate_To_demo_tours_page():
    driver = webdriver.Chrome(
        ChromeDriverManager().install())  # Install chrome driver exe as per browser version found in system

    driver.get("https://www.opera.com/download")
    driver.add_cookie({"name": "cookie_consent_essential", "domain": ".opera.com", "value": "true"})
    driver.refresh()

    sleep(1000)
    driver.quit()