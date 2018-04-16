import os
import pytest
from selenium import webdriver
import config


# helper method - enables us to specify a custom runtime flag and set a sensible default
# value gets passed through request variable
def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="http://the-internet.herokuapp.com",
                     help="base URL for the application under test")
    parser.addoption("--browser",
                     action="store",
                     default="firefox",
                     help="the name of the browser you want to test with")
# Decorators are a form of metadata. Adds additional functionality in your tests. Used for test setup/teardown
# In pytest we do this with a fixture (function gets called before test and also after)
# Method driver

# self is a required parameter for class methods
# request is a parameter made available to fixtures. It enables access to loads of things during a test run

@pytest.fixture
def driver(request):
        config.baseurl = request.config.getoption("--baseurl")
        config.browser = request.config.getoption("--browser")

        _geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver')
        _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver')

        if config.browser == "firefox":
            driver_ = webdriver.Firefox(executable_path=_geckodriver)
        elif config.browser == "chrome":
            driver_ = webdriver.Chrome(executable_path=_chromedriver)

        # part of method driver
        def quit():
            driver_.quit()

        # part of method driver. The function ends when the indentation becomes smaller
        # Actions passed to addfinalizer get executed after a test method completes
        request.addfinalizer(quit)
        return driver_