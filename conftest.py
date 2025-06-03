import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chromium")

@pytest.fixture(scope="session")
def browser_name(pytestconfig):
    return pytestconfig.getoption("browser")

@pytest.fixture
def page(browser_name):
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()
        yield page
        context.close()
        browser.close()
