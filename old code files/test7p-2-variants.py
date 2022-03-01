from selenium import webdriver
import time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert
#from bs4 import BeautifulSoup
#import numpy as np
#import pandas as pd
import os

# ===================== ПРЕКРАСНЫЙ ПРИМЕР БЕЗ ЗАПУСКА БРАУЗЕРА - ТО ЧТО МНЕ НАДО

link = "http://suninjuly.github.io/find_link_text"
text = str(math.ceil(math.pow(math.pi, math.e)*10000))
options = webdriver.ChromeOptions()
options.headless = True
#options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36")
browser = webdriver.Chrome(options=options)
try:
    browser.get(link)
    input0 = browser.find_element_by_link_text(text)
    input0.click()
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_css_selector('#country')
    input4.send_keys("Russia")
    #button = browser.find_element_by_css_selector('#submit_button')
    #button.click()
    push_submit = browser.find_element(By.XPATH, "//button[text()='Submit']")
    push_submit.click()
    print('\n')
    print(Alert(browser).text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла