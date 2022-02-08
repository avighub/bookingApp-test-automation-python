from selenium.webdriver.common.by import By


class CartPage():

    def __init__(self,driverInstance):
        self.driver = driverInstance


        self.cartpagetitle = "//span[contains(text(),'Your Cart')]"
        self.checkoutbtn = "checkout"


    def verfiycartpage(self):
        self.driver.find_element(By.XPATH, self.cartpagetitle).is_displayed

    def clickcheckoutbtn(self):
        self.driver.find_element(By.ID, self.checkoutbtn).click()


