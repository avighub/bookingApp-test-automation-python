from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import conftest
from PageObjects_Deepa.CartPage import CartPage
from PageObjects_Deepa.CheckOutOverviewPage import CheckoutOverviewPage
from PageObjects_Deepa.CheckOut_InformationPage import CheckoutInformationPage
from PageObjects_Deepa.LoginPage import LoginPage
from PageObjects_Deepa.ProductPage import ProductPage
from PageObjects_Deepa.UserFlow import UserFlow


class TestCheckoutOverviewPage():

    def test_CheckoutOverviewPage(self):

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
        checkoutinfo.enterlastname("seeba")
        checkoutinfo.enterpostalcode("12345")
        checkoutinfo.clickcontinuebtn()

        checkoutoverview = CheckoutOverviewPage(driver)
        checkoutoverview.verifycheckoutoverviewpage()
        checkoutoverview.clickfinishbtn()

        finalpage = UserFlow(driver)
        finalpage.verifycheckoutcomplete()
        finalpage.displayedmsg()
        finalpage.saucelabimage()


        driver.quit()
