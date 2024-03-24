from selenium.webdriver.common.by import By


class LoginPage:
    # Locators
    txtbox_email_Name = "email"
    txtbox_pwd_Name = "password"
    button_login_css = "input[class = 'btn btn-primary']"
    msg_myaccount_xpath = "//div[@id='content']//h2[1]"

    # COnstructor
    def __init__(self, driver_obj):
        self.driver_obj = driver_obj

    # Action Methods
    def setEmail(self, useremail):
        self.driver_obj.find_element(By.NAME, self.txtbox_email_Name).send_keys(useremail)
    def setPWD(self, userpwd):
        self.driver_obj.find_element(By.NAME, self.txtbox_pwd_Name).send_keys(userpwd)
    def clickLogin(self):
        self.driver_obj.find_element(By.CSS_SELECTOR, self.button_login_css).click()

    def isMyAccountPageExists(self):
        try:
            return self.driver_obj.find_element(By.LINK_TEXT, self.msg_myaccount_xpath).is_displayed()
        except:
            return False
    def MyAccPageText(self):
        try:
            return self.driver_obj.find_element(By.XPATH, self.msg_myaccount_xpath).text
        except:
            return False