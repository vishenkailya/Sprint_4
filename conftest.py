import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()
