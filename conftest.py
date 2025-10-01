import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Grid Hub URL
GRID_URL = "http://localhost:4444/wd/hub"

@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Remote(command_executor=GRID_URL,
                              options=options)
    yield driver  # This is where the testing happens
    driver.quit() # Teardown
