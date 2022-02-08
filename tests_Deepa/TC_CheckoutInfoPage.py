from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import conftest
from PageObjects_Deepa.CartPage import CartPage
from PageObjects_Deepa.CheckOut_InformationPage import CheckoutInformationPage
from PageObjects_Deepa.LoginPage import LoginPage
from PageObjects_Deepa.ProductPage import ProductPage


class TestCheckoutInfoPage():

    def test_checkoutinfopage(self):
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
        product.cartBtn()

        cart = CartPage(driver)
        cart.verfiycartpage()
        cart.clickcheckoutbtn()

        checkoutinfo = CheckoutInformationPage(driver)
        checkoutinfo.verifytitle()
        checkoutinfo.enterfirstname("deepa")
        sleep(2)
        checkoutinfo.enterlastname("seeba")
        sleep(2)
        checkoutinfo.enterpostalcode("12345")
        sleep(2)
        checkoutinfo.clickcontinuebtn()
        sleep(2)

        driver.quit()
