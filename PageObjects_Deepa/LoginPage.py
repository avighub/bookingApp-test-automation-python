from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self,driverInstance):
        self.driver = driverInstance

        self.usernameInput = "user-name"
        self.passwordInput = "password"
        self.loginbtn = "login-button"

    def NavigatetoLoginPage(self):
        self.driver.get("https://www.saucedemo.com/")

    def EnterUsername(self, username):
        self.driver.find_element(By.ID, self.usernameInput).send_keys(username)

    def EnterPassword(self, password):
        self.driver.find_element(By.ID, self.passwordInput).send_keys(password)

    def CLickLogin(self):
        self.driver.find_element(By.ID, self.loginbtn).click()

