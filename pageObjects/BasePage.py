import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import conftest

'''
BasePage has Base class which is responsible for :
- Initializing browser before every Test
- Quitting the browser after Test is completed

No more extra code should be written as this pages hould be short and clean
Add only those actions that you need to perform for any TestPages 
'''


class Base:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.BROWSER = conftest.BROWSER_NAME
        match self.BROWSER:
            case "chrome":
                print("Initiating Chrome driver")
                service = Service(ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=service)
            case "firefox":
                print("Initiating Firefox driver")
                service = Service(GeckoDriverManager().install())
                self.driver = webdriver.Firefox(service=service)
            # Default
            case _:
                print("Initiating Default: Chrome driver")
                service = Service(ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=service)

        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()
