from Pages.LoginPage import LoginPage
from Tests.BaseTest import BasePage


class LoginTest(BasePage):
    def test_login_page(self):
        loginPage = LoginPage(self.driver)
        loginPage.click_on_login()
        # loginPage.enter_email_id("marazislam@gmail.com")

