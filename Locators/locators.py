from selenium.webdriver.common.by import By


class SignInPageLocators(object):

    LOGIN_BTN = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[2]/a")
    SET_EMAIL = (By.ID, "login-email")
    CLICK_EMAIL_XPATH = (By.XPATH, "//*[@id=\"login-form\"]/button")


    # self.driver = driver
    # self.setEmailId = "login-email"
    # self.clickEmailXpath = "//*[@id=\"login-form\"]/button"
    # self.passwordXpath = "//*[@id=\"login-password\"]"
    # self.clickPassword = "//button[contains(.,'Sign in')]"
    # self.clickLogin = "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[2]/a"


