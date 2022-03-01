############################ НАКОНЕЦ ТО Я НАЧАЛ РАБОТАТЬ С FIREFOX И СДЕЛАЛ ЗАДАНИЕ С ДРУГИМ ДРАЙВЕРОМ !!!!!!!!!!!

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\geckodriver05feb\geckodriver.exe', options=options)
driver.get('http://suninjuly.github.io/get_attribute.html')

treasure = driver.find_element(By.ID, 'treasure')
x = treasure.get_attribute('valuex')
y = calc(x)

driver.find_element_by_id('answer').send_keys(y)

for selector in ('#robotCheckbox', '#robotsRule', '.btn'):
         driver.find_element(By.CSS_SELECTOR, selector).click()

#alert = driver.switch_to_alert() #FIREFOX НЕ УМЕЕТ ПЕРЕКЛЮЧАТЬСЯ НА АЛЕРТЫ
#print(alert.text)

time.sleep(10)
driver.quit()



############ ВАРИАНТ 2 -  ПРОСТО ПЕЧАТАЕТ В КОНСОЛЬ И ЗАПОЛНЯЕТ С ПОМОЩЬЮ ЦИКЛА

# import math
#
# from selenium import webdriver
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# def print_answer(remote: webdriver.Remote):
#     alert = remote.switch_to.alert
#     print(alert.text.split()[-1])
#     alert.accept()
#
#
# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/get_attribute.html"
# browser.get(link)
#
# try:
#     x_element = browser.find_element_by_id("treasure").get_attribute("valuex")
#     browser.find_element_by_id("answer").send_keys(calc(x_element))
#     elements_to_select = tuple(("[id = 'robotCheckbox']", "[id='robotsRule']", "button.btn.btn-default"))
#
#     for elem in elements_to_select:
#         browser.find_element_by_css_selector(elem).click()
#
#     print_answer(browser)
# finally:
#     browser.quit()



############## САМЫЙ КОРОТКИЙ ВАРИАНТ 1

# from selenium import webdriver
# from math import log, sin
#
# browser = webdriver.Chrome()
#
# # Открыть страницу http://suninjuly.github.io/get_attribute.html
# browser.get('http://suninjuly.github.io/get_attribute.html')
#
# # Найти на ней элемент-картинку/ Взять у этого элемента значение атрибута valuex
# valuex = browser.find_element_by_css_selector('[id = "treasure"]').get_attribute('valuex')
#
# # Посчитать математическую функцию от x, Ввести ответ в текстовое поле.
# browser.find_element_by_id('answer').send_keys(str(log(abs(12 * sin(int(valuex))))))
#
# # Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!". Нажать на кнопку Отправить.
# for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
#   browser.find_element_by_css_selector(selector).click()