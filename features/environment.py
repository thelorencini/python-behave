import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



def before_all(context):
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    context.driver = webdriver.Chrome(ROOT_DIR + "/chromedriver")


def before_scenario(context, scenario):
    context.driver.maximize_window()


def before_step(context, step):
    context.driver.implicitly_wait(7)
