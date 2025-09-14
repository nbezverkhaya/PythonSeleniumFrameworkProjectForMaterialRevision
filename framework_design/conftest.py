import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(""
        "--browser_name", action="store", default="firefox", help="browser selection"
    )

@pytest.fixture(scope="function")
def browser_instance(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
    yield driver
    driver.quit()