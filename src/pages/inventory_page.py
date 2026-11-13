"""SauceDemo inventory (products) page, plus the cart and checkout steps."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from src.pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    # Cart / checkout locators (same app, kept here so the flow reads as one story)
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def page_title(self):
        return self.get_text(self.TITLE)

    def item_count(self):
        return len(self.find_all(self.ITEMS))

    def item_names(self):
        return [el.text for el in self.find_all(self.ITEM_NAMES)]

    def item_prices(self):
        return [float(el.text.replace("$", "")) for el in self.find_all(self.ITEM_PRICES)]

    def add_item_to_cart_by_name(self, name):
        locator = (By.XPATH, f"//div[text()='{name}']/ancestor::div[@class='inventory_item']//button")
        self.click(locator)

    def sort_by(self, visible_text):
        Select(self.find(self.SORT_SELECT)).select_by_visible_text(visible_text)

    def cart_badge_count(self):
        return int(self.get_text(self.CART_BADGE))

    def open_cart(self):
        self.click(self.CART_LINK)

    def cart_item_count(self):
        return len(self.find_all(self.CART_ITEMS))

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def order_complete_header(self):
        return self.get_text(self.COMPLETE_HEADER)

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
