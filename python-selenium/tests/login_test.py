import pytest
from pages import login_page

class TestLogin():
    # Decorators are a form of metadata. Adds additional functionality in your tests. Used for test setup/teardown
    # In pytest we do this with a fixture (function gets called before test and also after)
    # Method driver
    @pytest.fixture()
    # self is a required parameter for class methods
    def login(self, driver):
        return login_page.LoginPage(driver)

    # Our test method starts with the word (that's how pytest knows it's a test)
    # driver method is passed in(remember it returns driver_ a browser instance)
    @pytest.mark.smoke
    def test_valid_credentials(self, login):
        login.with_("tomsmith", "SuperSecretPassword!")
        assert login.success_message_present()

    @pytest.mark.regression
    def test_invalid_credentials(self, login):
        login.with_("sefdsf", "gsddsvs")
        assert login.failure_message_present()