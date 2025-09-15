import pytest
from selenium import webdriver

import os
driver = None

def pytest_addoption(parser):
    parser.addoption(""
        "--browser_name", action="store", default="firefox", help="browser selection"
    )

@pytest.fixture(scope="function")
def browser_instance(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report,
    whenever a test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            os.makedirs(reports_dir, exist_ok=True)

            file_name = os.path.join(
                reports_dir, report.nodeid.replace("::", "_") + ".png"
            )

            print("file name is " + file_name)

            driver = item.funcargs.get("browser_instance", None)
            if driver is not None:
                driver.save_screenshot(file_name)

            if file_name:
                html = (
                    '<div><img src="%s" alt="screenshot" '
                    'style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>'
                ) % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def capture_screenshot(file_name):
    driver.get_screenshot_as_a_file(file_name)