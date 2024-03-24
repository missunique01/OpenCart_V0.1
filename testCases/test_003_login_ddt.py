import os
from utilities import XLUtils
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Login_DDT:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = os.path.abspath(os.curdir) + r"\testdata\OpenCart_LoginData.xlsx"

    def test_login_ddt(self,setup):
        self.logger.info("*** test_login_ddt started  ***")
        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        lst_status = []

        self.driver_obj = setup
        self.driver_obj.get(self.baseURL)
        self.logger.info("Launching Application")
        self.driver_obj.maximize_window()

        self.hp_obj = HomePage(self.driver_obj)
        self.lp_obj = LoginPage(self.driver_obj)
        self.myacc_obj = MyAccountPage(self.driver_obj)

        for r in range(2,self.rows+1):
            self.email = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtils.readData(self.path,"Sheet1",r,3)

            self.hp_obj.clickmyAccount()
            self.hp_obj.clickLogin()

            self.lp_obj.setEmail(self.email)
            self.lp_obj.setPWD(self.password)
            self.lp_obj.clickLogin()
            self.targetpage = self.lp_obj.MyAccPageText()
            print(self.targetpage)
            if self.exp == "Valid":
                if self.targetpage == "My Account":
                    lst_status.append("Pass")
                    self.myacc_obj.clicklogout()
                else:
                    lst_status.append("Fail")
            elif self.exp == "Invalid":
                if self.targetpage == "My Account":
                    lst_status.append("Fail")
                    self.myacc_obj.clicklogout()
                else:
                    lst_status.append("Pass")
        self.driver_obj.close()
        print(lst_status)

        # Final Validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("Test_login_DDT is completed")



