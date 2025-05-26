import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_launch_browser(browser):
    page = browser.new_page()
    page.goto("https://www.google.com")
    print('Chrome successfully opened')
    print(page.title())
    page.wait_for_timeout(3000)

