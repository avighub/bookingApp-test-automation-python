from selenium.webdriver.common.by import By


class ProductsPage():
    # Constructor
    def __init__(self, driverIntance):
        self.driver = driverIntance
        # Locators
        self.productPageHederTitle = "#header_container > div.header_secondary_container > span"
        self.cartBtn = "#shopping_cart_container > a"
        self.cartBtnQty = "#shopping_cart_container > a > span"

    def verify_productPage_is_displayed(self):
        self.driver.find_element(By.CSS_SELECTOR, self.productPageHederTitle).is_displayed()

    def clickAddToCartBtnByName(self, productName):
        addToCarBtnByName = (
            By.XPATH, f'"//div[text()={productName}]//parent::a//parent::div//parent::div//div/button"')
        self.driver.find_element(addToCarBtnByName).click()
