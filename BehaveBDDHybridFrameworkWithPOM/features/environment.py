from selenium import webdriver

from utilities import config_reader


def before_scenario(context, driver):
    browser_name = config_reader.read_configuration('basic info', 'browser')
    if browser_name.__eq__('chrome'):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__('firefox'):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__('edge'):
        context.driver = webdriver.Edge()
    context.driver.get(config_reader.read_configuration('basic info','url'))
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def after_scenario(context, driver):
    context.driver.quit()
