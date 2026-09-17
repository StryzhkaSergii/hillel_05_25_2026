import time

from playwright.sync_api import expect


def test_iframe(page):
    page.goto("https://demoqa.com/frames")
    frame = page.frame_locator("#frame1")
    time.sleep(5)
    expected_frame_text = frame.locator("#sampleHeading").inner_text()
    assert expected_frame_text == "This is a sample page"

def test_tab(page):
    page.goto("https://demoqa.com/browser-windows")
    with page.context.expect_page() as second_page_context:
        page.locator("#tabButton").click()

    second_page = second_page_context.value
    second_page.wait_for_load_state()
    expected_h1 = second_page.locator("#sampleHeading").inner_text()
    assert expected_h1 == "This is a sample page"
    expect(second_page).to_have_url("https://demoqa.com/sample")
    time.sleep(2)

    pages = page.context.pages
    first_page = pages[0]
    first_page.bring_to_front()
    time.sleep(2)
    expect(first_page).to_have_url("https://demoqa.com/browser-windows")

def test_dialog(page):
    page.goto("https://demoqa.com/alerts")
    page.on("dialog", handle_dialog)
    page.locator("#promtButton").click()
    assert page.locator("#promptResult").inner_text() == "You entered Введений текст"
    # page.screenshot(path="screenshots/test_dialog.png")
    time.sleep(2)

def test_dialog_api_example(get_user):
    print(get_user)


def test_dialog_failed(page):
    page.goto("https://demoqa.com/alerts")
    page.on("dialog", handle_dialog)
    page.locator("#promtButton").click()
    assert page.locator("#promptResult").inner_text() == "You entered failed"

def test_dialog_failed_with_video(video_context):
    page = video_context.new_page()
    page.goto("https://demoqa.com/alerts")
    page.on("dialog", handle_dialog)
    page.locator("#promtButton").click()
    assert page.locator("#promptResult").inner_text() == "You entered failed"

def handle_dialog(dialog):
    if dialog.type == "alert":
        # alert — тільки прийняти
        dialog.accept()

    elif dialog.type == "confirm":
        # confirm — можна прийняти або відхилити
        dialog.accept()  # або dialog.dismiss()

    elif dialog.type == "prompt":
        # prompt — можна ввести текст
        dialog.accept("Введений текст")