from selenium.webdriver.common.by import By


class HomePage(object):
    def __init__(self, driver, base_url=""):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
