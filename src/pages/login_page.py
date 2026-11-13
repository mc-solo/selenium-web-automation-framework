"""SauceDemo login page (https://www.saucedemo.com).

Demo credentials are the public ones shown on the login page itself:
standard_user / secret_sauce. No real account is used anywhere.
"""

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.utils import config_loader


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        return super().open(config_loader.get("urls", "saucedemo"))

    def login(self, username, password):
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def login_as_standard_user(self):
        return self.login(
            config_loader.get("saucedemo", "standard_user"),
            config_loader.get("saucedemo", "password"),
        )

    def error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
