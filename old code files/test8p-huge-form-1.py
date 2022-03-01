from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert

def bez_chrome():

   try:
   # browser = webdriver.Chrome()

    options = webdriver.ChromeOptions()
    options.headless = True

    browser = webdriver.Chrome(options=options)

    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_xpath("//*[@type='text']")
    print('\n --------------------- Я НАШЕЛ ЭЛЕМЕНТ И НАЧИНАЮ ЗАПОЛНЯТЬ ФОРМУ БЕЗ ЗАПУСКА БРАУЗЕРА -------------')
    for element in elements:
        element.send_keys("HUGE FORM")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    print('\n')
    print(Alert(browser).text)
    print('\n --------------------- ТЕСТ БЕЗ БРАУЗЕРА УСПЕШНО ЗАВЕРШЕН! -------------')

   finally:
     # успеваем скопировать код за 30 секунд
       time.sleep(3)
     # закрываем браузер после всех манипуляций
       browser.quit()

def with_chrome():

   try:
    print('\n --------------------- ЧЕРЕЗ 3 СЕКУНДЫ ЗАПУСКАЮ БРАУЗЕР -------------')
    # time.sleep(3)
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_xpath("//*[@type='text']")
    print('\n --------------------- БРАУЗЕР УСПЕШНО ЗАПУЩЕН И ИДЕТ ТЕСТ -------------')
    for element in elements:
        element.send_keys("HUGE FORM")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    print('\n')
    print(Alert(browser).text)

   finally:
     # успеваем скопировать код за 30 секунд
       time.sleep(3)
     # закрываем браузер после всех манипуляций
       browser.quit()

bez_chrome()

with_chrome()