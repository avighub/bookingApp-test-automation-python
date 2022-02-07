from selenium.webdriver.common.by import By


class ProductPage():

    def __init__(self, driverInstance):
        self.driver = driverInstance

        self.title = "//span[contains(text(),'Products')]"
        self.addtocartproduct = "add-to-cart-sauce-labs-backpack"
        self.cartbtn = "div.page_wrapper div:nth-child(1) div.header_container:nth-child(1) div.primary_header div.shopping_cart_container:nth-child(3) > a.shopping_cart_link"


    def verify_ProductPage(self):
        self.driver.find_element(By.XPATH, self.title).is_displayed()


    def addProductToCart(self):
        self.driver.find_element(By.ID, self.addtocartproduct).click()

    def cartBtn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.cartbtn).click()

