
from selenium.webdriver.common.by import By

# https://naveenautomationlabs.com/opencart/

class HomePage:
        # Locators
        nav_myaccount_linkText = "My Account"
        nav_registerButton_linkText = "Register"
        nav_loginButton_Linktext = "Login"

        # Constructor
        def __init__(self, driver_obj):
            self.driver_obj = driver_obj

        # Action Methods

        def clickmyAccount(self):
            self.driver_obj.find_element(By.LINK_TEXT, self.nav_myaccount_linkText).click()

        def clickRegbutton(self):
            self.driver_obj.find_element(By.LINK_TEXT, self.nav_registerButton_linkText).click()
        def clickLogin(self):
            self.driver_obj.find_element(By.LINK_TEXT, self.nav_loginButton_Linktext).click()