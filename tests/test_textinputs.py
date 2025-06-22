
import pytest
from pages.text_input_page import TextInputPage

class TestTextInputPage:
    def test_text_input_page(self, driver):
        input_page = TextInputPage(driver)

