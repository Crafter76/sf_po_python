import pytest
from selenium import webdriver
from pom import page_objects
from base import seleniumbase
from time import sleep

@pytest.mark.usefixtures('setup')
class TestHomePage:

    def test_homepage(self):
        page_objects.SearchHelper(self.driver).enter_word('Iphone 13')
        page_objects.SearchHelper(self.driver).click_on_the_search_button()
        # seleniumbase.SeleniumBase(self.driver).is_present('css', '.cq')
        # seleniumbase.SeleniumBase(self.driver).get_element_by_text('Смартфон Apple iPhone 13 128GB Midnight (MLNW3RU/A)')