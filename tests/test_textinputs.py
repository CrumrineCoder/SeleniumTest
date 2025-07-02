
import pytest
from pages.text_input_page import TextInputPage

class TestTextInputPage:
    def test_text_input_page(self, driver):
        input_page = TextInputPage(driver)
        test_text = "Hello World"
        input_page.edit_normal_input(test_text)

        value = input_page.get_normal_input_value()
        assert value == test_text
    def test_failed_input(self, driver):
        input_page = TextInputPage(driver)
        test_text = "Hello World"
        input_page.edit_normal_input(test_text)

        value = input_page.get_normal_input_value()
        assert value != test_text

