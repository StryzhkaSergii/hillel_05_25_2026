import time

import pytest


@pytest.mark.ui
def test_login_click_enter(login_page):
        login_page.open()
        inventory_page = login_page.login_valid_user("standard_user", "secret_sauce")

        time.sleep(5)
        inventory_page.sort_by("Price (low to high)")
        time.sleep(5)