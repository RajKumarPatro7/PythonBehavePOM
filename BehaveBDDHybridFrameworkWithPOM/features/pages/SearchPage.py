from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    failure_message_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_product(self, product):
        return self.driver.find_element(By.XPATH, "//img[contains(@title," + product + ")]").is_displayed()

    def display_message_displayed(self, message):
        print( self.driver.find_element(By.XPATH, self.failure_message_xpath).text)
        return self.driver.find_element(By.XPATH, self.failure_message_xpath).text.__contains__(message)
