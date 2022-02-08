from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import conftest
from PageObjects_Deepa.LoginPage import LoginPage
from PageObjects_Deepa.ProductPage import ProductPage


class TestProductPage():

    def test_ProductPage(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        driver = self.driver

        login = LoginPage(driver)
        login.NavigatetoLoginPage()
        login.EnterUsername(conftest.USERNAME_STD)
        login.EnterPassword(conftest.PASSWORD_STD)
        login.CLickLogin()

        product = ProductPage(driver)
        product.verify_ProductPage()
        product.addProductToCart()
        sleep(2)
        product.cartBtn()
        sleep(2)

        driver.quit()