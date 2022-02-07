from selenium.webdriver.common.by import By


class CheckoutOverviewPage():

    def __init__(self,driverInstance):
        self.driver = driverInstance

        self.checkoutoverview = "//span[contains(text(),'Checkout: Overview')]"
        self.finishbtn = "finish"


    def verifycheckoutoverviewpage(self):
        self.driver.find_element(By.XPATH, self.checkoutoverview).is_displayed()

    def clickfinishbtn(self):
        self.driver.find_element(By.ID, self.finishbtn).click()

