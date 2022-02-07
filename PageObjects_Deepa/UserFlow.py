from selenium.webdriver.common.by import By


class UserFlow():

    def __init__(self,driverInstance):

        self.driver = driverInstance

        self.checkoutcomplete = "//span[contains(text(),'Checkout: Complete!')]"
        self.displaymsg = "//h2[contains(text(),'THANK YOU FOR YOUR ORDER')]"
        self.image = "//body/div[@id='root']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='checkout_complete_container']/img[1]"


    def verifycheckoutcomplete(self):
        self.driver.find_element(By.XPATH, self.checkoutcomplete).is_displayed()

    def displayedmsg(self):
        self.driver.find_element(By.XPATH, self.displaymsg).is_displayed()

    def saucelabimage(self):
        self.driver.find_element(By.XPATH, self.image).is_displayed()



