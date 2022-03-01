from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

#проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots_radio: ", robots_checked)
    assert robots_checked is None

#проверяем значение атрибута disabled у кнопки Submit
    button = browser.find_element_by_css_selector('.btn')
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    assert button_disabled is None

#проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(10)
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit after 10sec: ", button_disabled)
    assert button_disabled is not None

    print('\n')

    print(people_radio.get_attribute("name"))
    # Напечатает ruler, т.е. текстовое значение аттрибута

    print(people_radio.get_attribute("checked"))
    # Напечатает true, т.е. факт того что аттрибут существует. Учтите что true это в данном случае строка, а не булево значение.

    print(people_radio.get_attribute("href"))
    # Напечатает None, т.к. аттрибут не существует. И это не строка а None-значение.

    print(people_radio.get_attribute("id")) #напечатает название id

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла









####### КРУТО УДОБНО ТАК КОММЕНТИТЬ  """""

"""""

# МОЙ ВАРИАНТ ПРОВЕРЯЕМ АТТРИБУТЫ
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    people_radio = browser.find_element(By.ID, "peopleRule")
    #people_radio1 = browser.find_element(By.XPATH, "//input[@id='peopleRule']")

    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    #assert people_checked is not None, "People radio is not selected by default"
    #assert people_checked == "true", "People radio is not selected by default"
    assert people_checked == "false", "People radio is not selected by default"

    #robots_radio = browser.find_element_by_id("robotsRule")
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None
    print("value of people radio: ", robots_checked)
    #time.sleep(13) #НЕ ПОЛУЧИЛОСЬ ПОМЕНЯТЬ АТТРИБУТ КНОПКИ НА АКТИВНЫЙ
    #button1 = browser.find_element(By.XPATH, "//button[@type='submit']")
    #button_atr_change = button1.setattribute('enabled')
    #button1.send_keys('enabled')
    time.sleep(1)

finally:
"""""
    #time.sleep(3)
    #browser.quit()

