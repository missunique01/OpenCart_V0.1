from selenium.webdriver.common.by import By

class AccountRegistrationPage:
    # Locators
    txtbox_firstname_name = "firstname"
    txtbox_lastname_name = "lastname"
    txtbox_email_name = "email"
    txtbox_telephone_name = "telephone"
    txtbox_password_id = "input-password"
    txtbox_conpassword_id = "input-confirm"
    checkbox_click_name = "agree"
    button_click_xpath = "//input[@class='btn btn-primary']"
    msg_success_tagname = "h1" # Your Account Has Been Created!

    # Constructor

    def __init__(self, driver_obj):
        self.driver_obj = driver_obj

    # Action methods
    def setFName(self, fname):
        firstnametxt = self.driver_obj.find_element(By.NAME, self.txtbox_firstname_name)
        firstnametxt.send_keys(fname)

    def setLName(self, lname):
        lastnametxt = self.driver_obj.find_element(By.NAME, self.txtbox_lastname_name)
        lastnametxt.send_keys(lname)

    def setEmail(self, email):
        emailtxt = self.driver_obj.find_element(By.NAME, self.txtbox_email_name)
        emailtxt.send_keys(email)

    def setTelephone(self,phone):
        telephonenum = self.driver_obj.find_element(By.NAME, self.txtbox_telephone_name)
        telephonenum.send_keys(phone)

    def setpwd(self, pwd):
        pwdtxt = self.driver_obj.find_element(By.ID, self.txtbox_password_id)
        pwdtxt.send_keys(pwd)

    def setconpwd(self,conpwd):
        conpwdtxt = self.driver_obj.find_element(By.ID,self.txtbox_conpassword_id)
        conpwdtxt.send_keys(conpwd)

    def clickcheckbox(self):
        self.driver_obj.find_element(By.NAME, self.checkbox_click_name).click()

    def clickcontinue(self):
        self.driver_obj.find_element(By.XPATH, self.button_click_xpath).click()

    def getconfirmmsg(self):
        try:
            return self.driver_obj.find_element(By.TAG_NAME,self.msg_success_tagname).text
        except:
            None

