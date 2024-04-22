import time

from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage
from features.pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    search_box_xpath = "//div[@id='search']/input"
    search_button_xpath = "//button[contains(@class,'btn btn-default btn-lg')]"

    def get_title_of_page(self):
        return self.driver.title

    def enter_product_into_search_field(self, product):
        BasePage.enter_text_into_field(self, "search_box_xpath", self.search_box_xpath, product)

    def click_on_search_button(self):
        BasePage.click_on_element(self, "search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)
