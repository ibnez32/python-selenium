import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin():
    # Decorators are a form of metadata. Adds additional functionality in your tests. Used for test setup/teardown
    # In pytest we do this with a fixture (function gets called before test and also after)
    # Method driver
    @pytest.fixture()
    def driver(self, request):
        #_geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver')
        driver = webdriver.Firefox(executable_path='/Users/ibnezabed/Desktop/selenium-guidebook-python-practice/python-selenium/vendor/geckodriver')

        def quit():
            driver.quit()

        request.addfinalizer(quit)
        return driver

    def test_valid_credentials(self, driver):
        driver.get("http://the-internet.herokuapp.com/login")
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button").click()
        assert(driver.find_element(By.CSS_SELECTOR, ".flash.success").is_displayed())

