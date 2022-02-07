from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import conftest
from PageObjects_Deepa.CartPage import CartPage
from PageObjects_Deepa.LoginPage import LoginPage
from PageObjects_Deepa.ProductPage import ProductPage


class TestCartPage():

    def test_cartpage(self):

        self.driver =  webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver

        login = LoginPage(driver)
        login.NavigatetoLoginPage()
        login.EnterUsername(conftest.USERNAME_STD)
        login.EnterPassword(conftest.PASSWORD_STD)
        login.CLickLogin()

        product = ProductPage(driver)
        product.verify_ProductPage()
        product.addProductToCart()
        product.cartBtn()

        cart = CartPage(driver)
        cart.verfiycartpage()
        sleep(2)
        cart.clickcheckoutbtn()
        sleep(2)

        driver.quit()

