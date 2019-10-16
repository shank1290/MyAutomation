import pytest
from selenium import webdriver
from base.drivers import GetWebDriver

@pytest.fixture()
def setUp():
    print("doing method level setup")
    yield
    print("doing method level setup teardown")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    wd = GetWebDriver(browser)
    driver = wd.getDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tear down")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType",help = "Type of OS")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
