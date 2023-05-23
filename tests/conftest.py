import pytest
from selene.support.shared import browser

@pytest.fixture()
def set_browser_size():
    browser.config.window_height = 1440
    browser.config.window_width = 720
    return browser

@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()
