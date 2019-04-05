import pytest
from selenium import webdriver


# define option name and default option
def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Type in browser type (chrome / firefox) ")


# Add support for another browsers below
@pytest.fixture(scope="module", autouse=True)
def driver(request):
    browser = request.config.getoption("--driver")
    if browser == 'chrome':
        browser = webdriver.Chrome()
        browser.maximize_window()
        return browser
    elif browser == 'firefox':
        browser = webdriver.Firefox()
        browser.maximize_window()
        return browser
