import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options

@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    #options.add_argument('--headless')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=800,600')
    return options

@pytest.fixture(scope='function')
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)
    return driver

@pytest.fixture
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://yandex.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()