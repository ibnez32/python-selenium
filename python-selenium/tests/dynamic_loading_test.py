import pytest
from selenium import webdriver
from pages import dynamic_loading_page

class TestDynamicLoading():
    # Decorators are a form of metadata. Adds additional functionality in your tests. Used for test setup/teardown
    # In pytest we do this with a fixture (function gets called before test and also after)
    # Method driver
    @pytest.fixture()
    # self is a required parameter for class methods
    # request is a parameter made available to fixtures. It enables access to loads of things during a test run
    def dynamic_loading(self, request):
        #_geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver')
        #driver_ = webdriver.Firefox(executable_path=_geckodriver)
        driver_ = webdriver.Firefox(executable_path='/Users/ibnezabed/Desktop/selenium-guidebook-python-practice/python-selenium/vendor/geckodriver')

        # part of method driver
        def quit():
            driver_.quit()
        # part of method driver. The function ends when the indentation becomes smaller
        # Actions passed to addfinalizer get executed after a test method completes
        request.addfinalizer(quit)
        return dynamic_loading_page.DynamicLoadingPage(driver_)

    def test_hidden_element(self, dynamic_loading):
        dynamic_loading.load_example("1")
        assert dynamic_loading.finish_text_present()

    def test_rendered_element(self, dynamic_loading):
        dynamic_loading.load_example("2")
        assert dynamic_loading.finish_text_present()