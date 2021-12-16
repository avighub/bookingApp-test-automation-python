from selenium.webdriver.common.by import By


class LoginPage():
    # Constructor
    def __init__(self, driverIntance):
        self.driver = driverIntance
        # Locators
        self.userNameInputTxt = "user-name"
        self.passwordInputTxt = "password"
        self.loginBtn = "login-button"

    def navigate_To_LoginPage(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_UserName(self, username):
        self.driver.find_element(By.ID, self.userNameInputTxt).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.passwordInputTxt).send_keys(password)

    def click_loginBtn(self):
        self.driver.find_element(By.ID, self.loginBtn).click()
