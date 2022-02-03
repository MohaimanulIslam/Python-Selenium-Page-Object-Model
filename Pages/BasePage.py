from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, diver, locator, by):
        self.driver = diver
        self.locator = locator
        self.by = by

        self.web_element = None

    def find(self):
        self.driver.find_element_by_id()
