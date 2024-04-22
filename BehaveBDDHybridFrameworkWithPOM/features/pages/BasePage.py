from selenium.webdriver.common.by import By


def determine_the_locator_type(locator_type):
    if locator_type.endswith("xpath"):
        return By.XPATH
    if locator_type.endswith("css_selector"):
        return By.CSS_SELECTOR


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator_type, locator_value):
        var = determine_the_locator_type(locator_type)
        self.driver.find_element(var, locator_value).click()

    def enter_text_into_field(self, locator_type, locator_value, text):
        var = determine_the_locator_type(locator_type)
        self.driver.find_element(var, locator_value).click()
        self.driver.find_element(var, locator_value).send_keys(text)
