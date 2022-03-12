import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.smoke
def test_guest_should_see_login_link(browser):
    link = f"https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    time.sleep(3)
    answer = math.log(int(time.time()))
    find_x = browser.find_element(By.XPATH, "//*[@placeholder='Type your answer here...']").send_keys(answer)
    logInBtn = browser.find_element(By.XPATH, "//*[@class='submit-submission']").click()
    time.sleep(3)
    find_class = browser.find_element(By.XPATH, "//*[@class='smart-hints__hint']")
    find_text = browser.find_element(By.XPATH, "//*[contains(text(), 'Correct!')]")
    print('\n текст = ',find_text)