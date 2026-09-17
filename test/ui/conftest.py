from pathlib import Path

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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Перевіряємо, чи тест впав
    if report.when == "call" and report.failed:
        # Отримуємо фікстуру page з тесту, якщо вона там є
        page = item.funcargs.get("page")
        if page:
            # Створюємо директорію для скріншотів, якщо її немає
            Path("screenshots").mkdir(exist_ok=True)
            # Зберігаємо скріншот з іменем тесту
            page.screenshot(path=f"screenshots/{item.name}.png")

@pytest.fixture
def video_context(browser):
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width":1280, "height":720}
    )
    yield context
    context.close()

@pytest.fixture
def get_user(page):
    response = page.request.get("https://gorest.co.in/public/v2/users/8614822")
    yield response.json()
    # page.request.post("url", data={})