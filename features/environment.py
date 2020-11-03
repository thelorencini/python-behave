import os
import platform
from selenium import webdriver





def before_all(context):
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if("Linux" in platform.platform()):
        system_file = "/chromedriver_linux"
    elif("Windows" in platform.platform()):
        system_file = "/chromedriver_windows.exe"
    else:
        raise Exception('Sistema não identificado')

    context.driver = webdriver.Chrome(ROOT_DIR + system_file)


def before_scenario(context, scenario):
    context.driver.maximize_window()


def before_step(context, step):
    context.driver.implicitly_wait(7)
