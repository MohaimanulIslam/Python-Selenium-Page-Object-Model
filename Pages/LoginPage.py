class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.setEmailId = "login-email"
        self.clickEmailXpath = "//*[@id=\"login-form\"]/button"
        self.passwordXpath = "//*[@id=\"login-password\"]"
        self.clickPassword = "//button[contains(.,'Sign in')]"
        self.clickLogin = "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[2]/a"

    def click_on_login(self):
        self.driver.find_element_by_xpath(self.clickLogin).click()

    def enter_email_id(self, email):
        self.driver.find_element_by_id(self.setEmailId).send_keys(email)
