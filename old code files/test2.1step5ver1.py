from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    find_x = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = find_x.text
    print(x)
    print('\n')

    y = calc(x)
    #z = str(math.log(abs(12*math.sin(int(x)))))
    print(y)
    print('\n')
    #print(z)

    send_answer = browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)
    time.sleep(1)
    robot_box = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
    time.sleep(1)
    robots_rule = browser.find_element(By.XPATH, "//label[@for='robotsRule']").click()
    time.sleep(1)
    submit_btn = browser.find_element(By.XPATH, "//button[@type='submit']").click()

  #ДОБАВЬ ЕЩЕ КОД НА СЧИТЫВАНИЕ АЛЕРТА И ПРОСМОТРИ РЕШЕНИЯ ДРУГИХ РЕБЯТ

finally:
    time.sleep(3)
   # browser.quit()


##def captcha():
