import configparser
import os

# config_file_path = os.path.abspath(os.path.join("..","configurations", "config.ini"))
# config_file_path = r'C:\Users\home\PycharmProjects\OpenCart_v0.1_SelPytest\configurations\config.ini'
config_file_path = os.path.abspath(os.curdir)+'\\configurations\\config.ini'
config = configparser.RawConfigParser()
config.read(config_file_path)
print(config_file_path)
# print(config.sections())
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url
    @staticmethod
    def getUserEmail():
        username = config.get('commonInfo','email')
        return username
    @staticmethod
    def getPassword():
        password = config.get('commonInfo','password')
        return password


# readconfig_obj = ReadConfig()
# app_url = readconfig_obj.getApplicationURL()
# print(app_url)
# print(ReadConfig.getApplicationURL())