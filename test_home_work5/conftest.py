import time

import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1600
    browser.config.window_height = 900
    browser.config.timeout = 10
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield

    time.sleep(10)
    browser.quit()
