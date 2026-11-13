"""Shopping tests for SauceDemo: inventory, sorting, cart, checkout."""

import pytest


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.cart
def test_inventory_lists_six_products(logged_in_inventory):
    assert logged_in_inventory.item_count() == 6


@pytest.mark.regression
def test_sort_by_price_low_to_high(logged_in_inventory):
    logged_in_inventory.sort_by("Price (low to high)")
    prices = logged_in_inventory.item_prices()
    assert prices == sorted(prices)


@pytest.mark.regression
def test_sort_by_name_z_to_a(logged_in_inventory):
    logged_in_inventory.sort_by("Name (Z to A)")
    names = logged_in_inventory.item_names()
    assert names == sorted(names, reverse=True)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.cart
def test_add_one_item_updates_cart_badge(logged_in_inventory):
    logged_in_inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    assert logged_in_inventory.cart_badge_count() == 1


@pytest.mark.regression
@pytest.mark.cart
def test_add_two_items_shows_both_in_cart(logged_in_inventory):
    logged_in_inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    logged_in_inventory.add_item_to_cart_by_name("Sauce Labs Bike Light")
    assert logged_in_inventory.cart_badge_count() == 2
    logged_in_inventory.open_cart()
    assert logged_in_inventory.cart_item_count() == 2


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.cart
def test_full_checkout_flow_completes_order(logged_in_inventory):
    logged_in_inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    logged_in_inventory.open_cart()
    logged_in_inventory.checkout()
    logged_in_inventory.fill_checkout_info("Wondwosen", "Asegid", "1000")
    logged_in_inventory.finish_checkout()
    assert "Thank you for your order" in logged_in_inventory.order_complete_header()
