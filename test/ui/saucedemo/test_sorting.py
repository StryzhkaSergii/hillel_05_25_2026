import time

import pytest


@pytest.mark.ui
def test_login_click_enter(login_page):
        login_page.open()
        inventory_page = login_page.login_valid_user("standard_user", "secret_sauce")

        inventory_page.sort_by("Price (low to high)")
        expect_sorted_prices = inventory_page.collect_price()

        assert expect_sorted_prices == sorted(expect_sorted_prices)