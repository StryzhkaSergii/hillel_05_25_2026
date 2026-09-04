import pytest

from core.pages.login_page import LoginPage


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {"headless":False,
            # "slow_mo":500,
            "args": ["--start-maximized"]}

@pytest.fixture(scope="session")
def browser_context_args():
    return {"no_viewport": True}

@pytest.fixture()
def login_page(page):
    return LoginPage(page)