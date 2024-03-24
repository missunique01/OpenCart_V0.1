import time
import os

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistration import AccountRegistrationPage
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen  # -- This is for logging---

class Test_001_AccReg:
    # baseURL = "https://naveenautomationlabs.com/opencart/index.php?route=common/home"
    # readconfig_obj = ReadConfig()
    # baseURL = readconfig_obj.getApplicationURL()
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # FOr logging
    # print(baseURL)
    @pytest.mark.regression
    def test_account_reg(self, setup):
        self.driver_obj = setup
        self.logger.info("*** test_001_AccountRegistration started  ***")
        self.driver_obj.get(self.baseURL)
        self.logger.info("Launching Application")
        self.driver_obj.maximize_window()
        # # Create the Homepage object and call the methods
        self.hp_obj = HomePage(self.driver_obj)
        self.logger.info("Clicking on My Account")
        self.hp_obj.clickmyAccount()
        self.logger.info("Clicking on Register")
        self.hp_obj.clickRegbutton()

        # Create the account register object and call the methods
        self.logger.info("Provide customer details for registration")
        self.regpage_obj = AccountRegistrationPage(self.driver_obj)

        self.regpage_obj.setFName("Abdu")
        self.regpage_obj.setLName("Nazz")
        # self.regpage_obj.setEmail("abdu@gmail.com")
        # As the gmail should be unique we need create a utility file for dynamic gmail
        self.email = randomString.random_string_generator() + "@gmail.com"
        self.regpage_obj.setEmail(self.email)
        self.regpage_obj.setTelephone(1235481206)
        self.regpage_obj.setpwd("Nazma123")
        self.regpage_obj.setconpwd("Nazma123")
        self.regpage_obj.clickcheckbox()
        self.regpage_obj.clickcontinue()
        self.confirmmsg = self.regpage_obj.getconfirmmsg()
        # self.driver_obj.close()
        if self.confirmmsg == "Your Account Has Been Created!":
            self.logger.info("Account Registration is passed")
            assert True
        else:
            self.driver_obj.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg.png")
            self.logger.info("Account Registration is Failed")
            self.driver_obj.close()
            assert False
        self.logger.info("test_001_AccountRegistration Completed")

