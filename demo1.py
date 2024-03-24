
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


service_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless")
driver_obj = webdriver.Chrome(service=service_obj, options=options)
driver_obj.implicitly_wait(10)
driver_obj.get("https://naveenautomationlabs.com/opencart/")

driver_obj.find_element(By.LINK_TEXT,"My Account").click()
driver_obj.find_element(By.LINK_TEXT,"Login").click()

driver_obj.find_element(By.NAME,"email").send_keys("abdu@gmail.com")
driver_obj.find_element(By.NAME,"password").send_keys("Nazma123@")
driver_obj.find_element(By.CSS_SELECTOR,"input[class = 'btn btn-primary']").click()
targetpage1 = driver_obj.find_element(By.XPATH,"//div[@id='content']//h2[1]").is_displayed()
targetpage =  driver_obj.find_element(By.XPATH,"//div[@id='content']//h2[1]").text
print(targetpage)
if targetpage == "My Account":
    print("Pass")
    # driver_obj.find_element(By.XPATH,"//ul[contains(@class,'dropdown-menu-right')]").click()
    driver_obj.find_element(By.LINK_TEXT,"Logout").click()
    print("Logged Out Succcefully ")
else:
    print("Fail")