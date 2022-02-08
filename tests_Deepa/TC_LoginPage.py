
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from PageObjects_Deepa.LoginPage import LoginPage


class TestLoginPage():

    def test_LoginPage(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        driver = self.driver

        login = LoginPage(driver)
        login.NavigatetoLoginPage()
        login.EnterUsername("standard_user")
        login.EnterPassword("secret_sauce")
        login.CLickLogin()

        driver.quit()


