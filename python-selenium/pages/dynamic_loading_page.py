from selenium.webdriver.common.by import By
from base_page import BasePage

class DynamicLoadingPage(BasePage):
    _start_button = {"by": By.CSS_SELECTOR, "value": "#start button"}
    _finish_text = {"by": By.ID, "value": "finish"}

    def __init__(self, driver):
        self.driver = driver

    def load_example(self, example_number):
        self._visit("/dynamic_loading/" + example_number)
        self._click(self._start_button)

    # timeout specifies how long we'd like selenium to wait for an element to be displayed before giving up
    def finish_text_present(self):
        return self._wait_for_is_displayed(self._finish_text, 10)

