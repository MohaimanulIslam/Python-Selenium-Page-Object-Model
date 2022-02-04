from Locators.locators import SignInPageLocators
from Pages.BasePage import HomePage


class LoginPage(HomePage):

    def __init__(self, driver):
        self.locator = SignInPageLocators
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def click_on_login(self):
        self.find_element(*self.locator.LOGIN_BTN).click()

    # def enter_email_id(self, email):
    #     self.driver.find_element_by_id(self.setEmailId).send_keys(email)
