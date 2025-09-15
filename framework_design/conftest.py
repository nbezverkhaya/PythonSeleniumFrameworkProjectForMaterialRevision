import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(""
        "--browser_name", action="store", default="firefox", help="browser selection"
    )

@pytest.fixture(scope="function")
def browser_instance(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()