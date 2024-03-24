import logging
import os
class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        # file handler object
        logs_dir = r'C:\Users\home\PycharmProjects\OpenCart_v0.1_SelPytest\logs'
        log_file_path = os.path.join(logs_dir, 'automation.logs')
        filehandler_obj = logging.FileHandler(log_file_path)

        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler_obj.setFormatter(formatter)
        logger.addHandler(filehandler_obj)

        logger.setLevel(logging.DEBUG)
        return logger
        # # path= r'C:\Users\home\PycharmProjects\OpenCart_v0.1_SelPytest\logs'
        # # path = os.path.abspath(os.curdir) + r'\\logs\\automation.log'
        # logging.basicConfig(filename=path+ 'automation.log',
        #                     format="%(asctime)s :%(levelname)s :%(message)s",
        #                     datefmt='%m/%d/%Y %I:%M:%S %p')

