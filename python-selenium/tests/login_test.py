import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages import login_page

class TestLogin():
    # Decorators are a form of metadata. Adds additional functionality in your tests. Used for test setup/teardown
    # In pytest we do this with a fixture (function gets called before test and also after)
    # Method driver
    @pytest.fixture()
    # self is a required parameter for class methods
    # request is a parameter made available to fixtures. It enables access to loads of things during a test run
    def login(self, request):
        #_geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver')
        #driver_ = webdriver.Firefox(executable_path=_geckodriver)
        driver_ = webdriver.Firefox(executable_path='/Users/ibnezabed/Desktop/selenium-guidebook-python-practice/python-selenium/vendor/geckodriver')
        # part of method driver
        def quit():
            driver_.quit()
        # part of method driver. The function ends when the indentation becomes smaller
        # Actions passed to addfinalizer get executed after a test method completes
        request.addfinalizer(quit)
        return login_page.LoginPage(driver_)

    # Our test method starts with the word (that's how pytest knows it's a test)
    # driver method is passed in(remember it returns driver_ a browser instance)
    def test_valid_credentials(self, login):
        login.with_("tomsmith", "SuperSecretPassword!")
        assert login.success_message_present()

    def test_invalid_credentials(self, login):
        login.with_("sefdsf", "gsddsvs")
        assert login.failure_message_present()