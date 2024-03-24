from datetime import datetime

import pytest
import os
from pytest_metadata.plugin import metadata_key
from selenium import webdriver


# This will get the value from CLI/hook
# This is not a normal method (Special type of method) Thats why it is called as HOOK
def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def setup(request):
    # This will return the broswer value to the setup method
    browser = request.config.getoption("browser")
    if browser == "chrome":
        from selenium.webdriver.chrome.options import Options
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver_obj = webdriver.Chrome(options=options)
        print("Launching Chrome Browser")
        driver_obj.implicitly_wait(10)
        return driver_obj
    elif browser == "edge":
        from selenium.webdriver.edge.options import Options
        options = webdriver.EdgeOptions()
        driver_obj = webdriver.Edge(options=options)
        print("Launching Edge Browser")
        driver_obj.implicitly_wait(10)
        return driver_obj
    else:
        from selenium.webdriver.chrome.options import Options
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver_obj = webdriver.Chrome(options=options)
        print("Launching Chrome Browser By default")
        driver_obj.implicitly_wait(10)
        return driver_obj
# For generating the HTML Report we need to add fixtures and HOOKS

# It is hook for Adding Environment info to HTML Report
# @pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = (os.path.abspath(os.curdir) + "\\reports\\"
                                  + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html")
    config.stash[metadata_key]["Project Name"] = "Open Cart DEMO"
    config.stash[metadata_key]["Module Name"] = "Register Module"
    config.stash[metadata_key]["Tester Name"] = "Nazma"

# It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# Specifying report folder location and save report with timestamp
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     config.option.htmlpath = (os.path.abspath(os.curdir) + "\\reports\\"
#                               + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html")
