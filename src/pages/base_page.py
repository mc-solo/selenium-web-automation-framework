"""Base page: the shared building blocks every page object uses.

All waits here are explicit (WebDriverWait + expected conditions).
There is no implicit wait and no time.sleep() anywhere in the suite:
a test waits for exactly the condition it needs, then moves on.
"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.utils import config_loader


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            config_loader.getint("browser", "explicit_wait", fallback=10),
        )

    def open(self, url):
        self.driver.get(url)
        return self

    @property
    def title(self):
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url

    def find(self, locator):
        """Wait until the element is visible, then return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find_clickable(locator).click()

    def type_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def wait_for_url_to_contain(self, fragment):
        return self.wait.until(EC.url_contains(fragment))
