from base import seleniumbase
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from time import sleep

class MainPageLocator:
    LOCATOR_SEARCH = {'by':'CSS', 'name':'#text'}
    LOCATOR_SEARCH_BUTTON = {'by':'xpath', 'name':'//*[@type="submit"]'}

class SearchHelper(seleniumbase.SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_word(self, word: str) -> WebElement:
        search_field = self.is_present(MainPageLocator.LOCATOR_SEARCH['by'], MainPageLocator.LOCATOR_SEARCH['name'])
        search_field.send_keys(word)
        search_field.send_keys(Keys.ENTER)
        return search_field

    def click_on_the_search_button(self):
        return self.is_visible(MainPageLocator.LOCATOR_SEARCH_BUTTON['by'], MainPageLocator.LOCATOR_SEARCH_BUTTON['name'])
