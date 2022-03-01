import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

  #  input1 = browser.find_element_by_name("first_name")
    input1 = browser.find_element_by_tag_name('input')
   # input1 = browser.find_element_by_tag_name("first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
 #   input3 = browser.find_element(By.NAME, "firstname")
 #   input3 = browser.find_element(By.CLASS_NAME, "form-control.city") #не работало когда ставил точку в начале .form-control.city
#    input3 = browser.find_element(By.CLASS_NAME, "city") #если просто класс, то вообще не нужна точка перед классом
    input3 = browser.find_element_by_css_selector(".form-control.city") #при поиске через ССС_Селектор нужны обе точки

    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла