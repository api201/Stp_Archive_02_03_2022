# Параметризация тестов для выбора браузера
from selenium.webdriver.firefox.options import Options
import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
drivers = ['webdriver.Chrome()', "webdriver.Firefox(executable_path=r'C:\geckodriver05feb\geckodriver.exe', options=options)"]

#COOL SETTINGS, NOW ITS WORKING IMMEDIATELY IN TWO DIFFERENT BROWSERS - CHROME AND FIREFOX

@pytest.mark.parametrize('browser', drivers)
def test_guest_should_see_login_link(browser):
    with eval(browser) as br:
        br.get(link)
        br.find_element_by_css_selector("#login_link")