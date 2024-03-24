import os

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    user = ReadConfig.getUserEmail()
    pwd = ReadConfig.getPassword()
    @pytest.mark.sanity
    def test_login(self,setup):

        self.driver_obj = setup
        self.logger.info("*** test_login started  ***")
        self.driver_obj.get(self.baseURL)
        self.logger.info("Launching Application")
        self.driver_obj.maximize_window()

        # # Create the Homepage object and call the methods
        self.hp_obj = HomePage(self.driver_obj)
        self.logger.info("Clicking on My Account")
        self.hp_obj.clickmyAccount()
        self.logger.info("Clicking on Login")
        self.hp_obj.clickLogin()

        # Create the Login Page object and call the methods
        self.logger.info("Provide customer details for Logging in")
        self.logpage_obj = LoginPage(self.driver_obj)
        self.logpage_obj.setEmail(self.user)
        self.logpage_obj.setPWD(self.pwd)
        self.logpage_obj.clickLogin()
        self.targetpage = self.logpage_obj.MyAccPageText()
        if self.targetpage == "My Account":
            assert True
        else:
            self.driver_obj.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg.png")
            self.logger.info("Account Login is Failed")
            assert False
        self.driver_obj.close()
        self.logger.info("test_login is  Completed")

