"""Shared fixtures: one fresh browser per test, closed afterwards.

A fresh driver per test keeps tests independent: a failure in one
test cannot leave state behind for the next one.
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.pages.inventory_page import InventoryPage
from src.pages.login_page import LoginPage
from src.pages.todo_page import TodoPage
from src.utils.driver_factory import create_driver


@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)


@pytest.fixture
def todo_page(driver):
    return TodoPage(driver)


@pytest.fixture
def logged_in_inventory(login_page, inventory_page):
    """Log in with the public demo user and land on the products page."""
    login_page.open().login_as_standard_user()
    inventory_page.wait_for_url_to_contain("inventory.html")
    return inventory_page
