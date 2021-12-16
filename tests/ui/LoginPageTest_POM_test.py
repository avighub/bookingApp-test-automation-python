# Using driver exe - Not so convinient way
from time import sleep

import pytest

from pageObjects.BasePage import Base
from pageObjects.LoginPage import LoginPage
from pageObjects.ProductsPage import ProductsPage


@pytest.mark.usefixtures('set_up')
class TestLogin(Base):
    # POM
    def test_navigateToLogin(self):
        driver = self.driver
        login = LoginPage(driver)
        login.navigate_To_LoginPage()
        sleep(0.5)

    def test_navigate_to_ProductsPage(self):
        # Preparation
        driver = self.driver
        login = LoginPage(driver)

        # Step 1 : Login
        login.navigate_To_LoginPage()
        login.enter_UserName("standard_user")
        login.enter_password("secret_sauce")
        login.click_loginBtn()
        sleep(1)

        #Step 2: Products Page
        productsPage = ProductsPage(driver)
        productsPage.verify_productPage_is_displayed()
