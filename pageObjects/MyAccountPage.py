from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyAccountPage:

    # Locator
    # btn_myacct_xpath = "//ul[contains(@class,'dropdown-menu-right')]"
    btn_logout_linktext = "Logout"
     # Constructor
    def __init__(self,driver_obj):
        self.driver_obj = driver_obj
     # Action Methods
    def clicklogout(self):
        WebDriverWait(self.driver_obj,10).until(
            EC.element_to_be_clickable((By.LINK_TEXT,self.btn_logout_linktext))).click()
