from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
        driver.maximize_window()
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):  #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()

def browser(request):
    return request.config.getoption("--browser")

# TERMINAL: pytest -s -v testCases/test_login.py --browser chrome
# TERMINAL: pytest -s -v testCases/test_login.py --browser firefox

# PARALLEL TEST RUN (in this version of pytest, it brakes parallel testing)
#TERMINAL: pytest -s -v -n=2 testCases/test_login.py --browser chrome --> n=number of test cases
#TERMINAL: pytest -s -v -n=2 testCases/test_login.py --browser firefox --> n=number of test cases


# PYTEST HTML REPORTS

#It is hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Nejla'

#It is hook for delete/modify environment info to HTML Reports
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)










