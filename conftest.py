import pytest
from selenium import webdriver


@ pytest.fixture
def driver():
    # open chrome browser
    driver = webdriver.Chrome()
    # to maximize the browser window
    driver.maximize_window()
    #give the driver to the test
    yield driver
    #close the browser after the test
    driver.quit()

