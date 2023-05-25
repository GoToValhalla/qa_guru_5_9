import pytest
from selene.support.shared import browser

@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.driver.set_window_size(1920, 1080)
    yield

    browser.quit()
