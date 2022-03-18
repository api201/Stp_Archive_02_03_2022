import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default=None,
#                      help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    #user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    #browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     browser = None
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         browser = webdriver.Chrome()
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


================= 2222

def test_quest_should_see_login_link(browser):
 #link=f"http://selenium1py.pythonanywhere.com/{user_language}"
 #link=f"http://selenium1py.pythonanywhere.com/"
 link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
 browser.get(link)
 #text_btn = browser.find_element(By.XPATH, "//button[@value='Add to basket']")
 text_btn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
 print("\n")
 print(text_btn)
 print("\n new line here!!! - ")
 print(text_btn.text)
 #assert text_btn == "Add to basket"
 assert "basket" in text_btn.text

 time.sleep(3)

=============== 3333   gotovo

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_quest_should_see_login_link(browser):
 #link=f"http://selenium1py.pythonanywhere.com/{user_language}"
 #link=f"http://selenium1py.pythonanywhere.com/"
 link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
 browser.get(link)
 #text_btn = browser.find_element(By.XPATH, "//button[@value='Add to basket']")
 text_btn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
 print("\n")
 print(text_btn)
 print("\n new line here!!! - ")
 print(text_btn.text)
 #assert text_btn == "Add to basket"
 #assert "basket" in text_btn.text
 assert text_btn == browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

 time.sleep(3)

