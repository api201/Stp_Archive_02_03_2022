from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time

browser = webdriver.Chrome()
url = 'http://suninjuly.github.io/xpath_examples'

try:
    browser.get(url)
    browser.maximize_window()

    btn1 = browser.find_element_by_css_selector(".btn") #кликает только на первую кнопку
    btn1.click()
    sleep(1)
    btn2 = browser.find_element_by_css_selector(".btn:nth-child(2)") #кликает на вторую кнопку ура
    btn2.click()
    sleep(1)
    #btn3 = browser.find_element_by_css_selector(".btn") #кликает только на первую кнопку
    #btn3 = browser.find_element_by_css_selector(".btn:nth-child(4)") #кликает на четвертую кнопку
    btn3 = browser.find_element_by_css_selector("div:nth-child(2) button:nth-child(3)") #кликает на седьмую кнопку
    btn3.click()

    vceknopki = browser.find_elements_by_css_selector(".btn")

    print(len(vceknopki))
    print(vceknopki)
    print(len(vceknopki))

    assert len(vceknopki) == 8

    #теперь надо найти 8 элементов и убедиться что их 8
    sleep(1)

except Exception as errors:
       print(f' ----- БРАТУХА ТУТ У ТЕБЯ ОШИБОЧКА КАКАЯ-ТО ЗАКРАЛАСЬ ----  | {errors}')

finally:
    print('\n ================ ТЕСТ УСПЕШНО ПРОЙДЕТ! РАСХОДИМСЯ ПОСОНЫ!!!! ================')
    sleep(1)
    browser.quit()