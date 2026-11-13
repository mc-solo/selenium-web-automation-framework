"""TodoMVC page (https://demo.playwright.dev/todomvc).

A plain React todo app. Good for testing add / complete / filter /
delete flows without any login.
"""

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.pages.base_page import BasePage
from src.utils import config_loader


class TodoPage(BasePage):
    NEW_TODO = (By.CLASS_NAME, "new-todo")
    TODO_ITEMS = (By.CSS_SELECTOR, ".todo-list li")
    TODO_LABELS = (By.CSS_SELECTOR, ".todo-list li label")
    TOGGLE_ALL = (By.CLASS_NAME, "toggle-all")
    CLEAR_COMPLETED = (By.CLASS_NAME, "clear-completed")
    ITEMS_LEFT = (By.CLASS_NAME, "todo-count")
    FILTER_ALL = (By.XPATH, "//a[text()='All']")
    FILTER_ACTIVE = (By.XPATH, "//a[text()='Active']")
    FILTER_COMPLETED = (By.XPATH, "//a[text()='Completed']")

    def open(self):
        return super().open(config_loader.get("urls", "todomvc"))

    def add_todo(self, text):
        field = self.find(self.NEW_TODO)
        field.send_keys(text + Keys.ENTER)

    def todo_texts(self):
        return [el.text for el in self.find_all(self.TODO_LABELS)]

    def todo_count(self):
        return len(self.driver.find_elements(*self.TODO_ITEMS))

    def items_left_text(self):
        return self.get_text(self.ITEMS_LEFT)

    def toggle_todo_by_text(self, text):
        locator = (By.XPATH, f"//label[text()='{text}']/preceding-sibling::input[@class='toggle']")
        self.click(locator)

    def toggle_all(self):
        self.click(self.TOGGLE_ALL)

    def clear_completed(self):
        self.click(self.CLEAR_COMPLETED)

    def filter_active(self):
        self.click(self.FILTER_ACTIVE)

    def filter_completed(self):
        self.click(self.FILTER_COMPLETED)

    def filter_all(self):
        self.click(self.FILTER_ALL)

    def delete_todo_by_text(self, text):
        label = (By.XPATH, f"//label[text()='{text}']")
        element = self.find(label)
        ActionChains(self.driver).move_to_element(element).perform()
        destroy = (By.XPATH, f"//label[text()='{text}']/following-sibling::button[@class='destroy']")
        self.click(destroy)
