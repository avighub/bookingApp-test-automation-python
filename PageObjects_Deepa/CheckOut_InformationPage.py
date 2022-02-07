from selenium.webdriver.common.by import By


class CheckoutInformationPage():

    def __init__(self,driverInstance):
        self.driver = driverInstance


        self.checkoutinformationpagetitle = "//span[contains(text(),'Checkout: Your Information')]"
        self.firstname = "first-name"
        self.lastname = "last-name"
        self.postalcode = "postal-code"
        self.continuebtn = "continue"


    def verifytitle(self):
        self.driver.find_element(By.XPATH,self.checkoutinformationpagetitle).is_displayed()

    def enterfirstname(self, firstname):
        self.driver.find_element(By.ID, self.firstname).send_keys(firstname)

    def enterlastname(self, lastname):
        self.driver.find_element(By.ID, self.lastname).send_keys(lastname)

    def enterpostalcode(self, postalcode):
        self.driver.find_element(By.ID, self.postalcode).send_keys(postalcode)

    def clickcontinuebtn(self):
        self.driver.find_element(By.ID, self.continuebtn).click()