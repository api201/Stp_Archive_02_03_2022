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
def test_guest_1(browser):
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

def test_guest_2(browser):
    link = f"https://stepik.org/lesson/236896/step/1"
    browser.get(link)
    time.sleep(3)
    answer = math.log(int(time.time()))
    find_x = browser.find_element(By.XPATH, "//*[@placeholder='Type your answer here...']").send_keys(answer)
    logInBtn = browser.find_element(By.XPATH, "//*[@class='submit-submission']").click()
    time.sleep(3)
    find_class = browser.find_element(By.XPATH, "//*[@class='smart-hints__hint']")
    find_text = browser.find_element(By.XPATH, "//*[contains(text(), 'Correct!')]")
    print('\n текст = ',find_text)

def test_guest_3(browser):
    link = f"https://stepik.org/lesson/236897/step/1"
    browser.get(link)
    time.sleep(3)
    answer = math.log(int(time.time()))
    find_x = browser.find_element(By.XPATH, "//*[@placeholder='Type your answer here...']").send_keys(answer)
    logInBtn = browser.find_element(By.XPATH, "//*[@class='submit-submission']").click()
    time.sleep(3)
    find_class = browser.find_element(By.XPATH, "//*[@class='smart-hints__hint']")
    find_text = browser.find_element(By.XPATH, "//*[contains(text(), 'Correct!')]")
    print('\n текст = ',find_text)

def test_guest_4(browser):
    link = f"https://stepik.org/lesson/236898/step/1"
    browser.get(link)
    time.sleep(3)
    answer = math.log(int(time.time()))
    find_x = browser.find_element(By.XPATH, "//*[@placeholder='Type your answer here...']").send_keys(answer)
    logInBtn = browser.find_element(By.XPATH, "//*[@class='submit-submission']").click()
    time.sleep(3)
    find_class = browser.find_element(By.XPATH, "//*[@class='smart-hints__hint']")
    find_text = browser.find_element(By.XPATH, "//*[contains(text(), 'Correct!')]")
    print('\n текст = ',find_text)

def test_guest_5(browser):
    link = f"https://stepik.org/lesson/236899/step/1"
    browser.get(link)
    time.sleep(3)
    answer = math.log(int(time.time()))
    find_x = browser.find_element(By.XPATH, "//*[@placeholder='Type your answer here...']").send_keys(answer)
    logInBtn = browser.find_element(By.XPATH, "//*[@class='submit-submission']").click()
    time.sleep(3)
    find_class = browser.find_element(By.XPATH, "//*[@class='smart-hints__hint']")
    find_text = browser.find_element(By.XPATH, "//*[contains(text(), 'Correct!')]")
    print('\n текст = ',find_text)

def test_guest_6(browser):
    link = f"https://stepik.org/lesson/236903/step/1"
    browser.get(link)
    time.sleep(3)
    answer = math.log(int(time.time()))
    find_x = browser.find_element(By.XPATH, "//*[@placeholder='Type your answer here...']").send_keys(answer)
    logInBtn = browser.find_element(By.XPATH, "//*[@class='submit-submission']").click()
    time.sleep(3)
    find_class = browser.find_element(By.XPATH, "//*[@class='smart-hints__hint']")
    find_text = browser.find_element(By.XPATH, "//*[contains(text(), 'Correct!')]")
    print('\n текст = ',find_text)

def test_guest_7(browser):
    link = f"https://stepik.org/lesson/236904/step/1"
    browser.get(link)
    time.sleep(3)
    answer = math.log(int(time.time()))
    find_x = browser.find_element(By.XPATH, "//*[@placeholder='Type your answer here...']").send_keys(answer)
    logInBtn = browser.find_element(By.XPATH, "//*[@class='submit-submission']").click()
    time.sleep(3)
    find_class = browser.find_element(By.XPATH, "//*[@class='smart-hints__hint']")
    find_text = browser.find_element(By.XPATH, "//*[contains(text(), 'Correct!')]")
    print('\n текст = ',find_text)

def test_guest_8(browser):
    link = f"https://stepik.org/lesson/236905/step/1"
    browser.get(link)
    time.sleep(3)
    answer = math.log(int(time.time()))
    find_x = browser.find_element(By.XPATH, "//*[@placeholder='Type your answer here...']").send_keys(answer)
    logInBtn = browser.find_element(By.XPATH, "//*[@class='submit-submission']").click()
    time.sleep(3)
    find_class = browser.find_element(By.XPATH, "//*[@class='smart-hints__hint']")
    find_text = browser.find_element(By.XPATH, "//*[contains(text(), 'Correct!')]")
    print('\n текст = ',find_text)