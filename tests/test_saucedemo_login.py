"""Login tests for SauceDemo (https://www.saucedemo.com).

Uses only the public demo credentials shown on the login page itself.
"""

import pytest

from src.utils import config_loader


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login
def test_valid_login_lands_on_inventory(login_page, inventory_page):
    login_page.open().login_as_standard_user()
    inventory_page.wait_for_url_to_contain("inventory.html")
    assert inventory_page.page_title() == "Products"


@pytest.mark.regression
@pytest.mark.login
def test_locked_out_user_sees_error(login_page):
    login_page.open().login(
        config_loader.get("saucedemo", "locked_out_user"),
        config_loader.get("saucedemo", "password"),
    )
    assert "locked out" in login_page.error_message()


@pytest.mark.regression
@pytest.mark.login
def test_wrong_password_sees_error(login_page):
    login_page.open().login("standard_user", "wrong_password")
    assert "Username and password do not match" in login_page.error_message()


@pytest.mark.regression
@pytest.mark.login
def test_empty_login_sees_error(login_page):
    login_page.open().login("", "")
    assert "Username is required" in login_page.error_message()


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login
def test_logout_returns_to_login_page(logged_in_inventory, login_page):
    logged_in_inventory.logout()
    assert login_page.is_visible(login_page.USERNAME)
