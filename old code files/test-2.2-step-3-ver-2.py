from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    #browser.get("http://suninjuly.github.io/selects2.html")
    find_x1 = browser.find_element(By.ID, "num1") #нашли элемент 1
    find_x2 = browser.find_element(By.XPATH, "//*[@id='num2']") #нашли элемент 2
    x1 = find_x1.text #записал в переменную текст из элемента
    x2 = find_x2.text #записал в переменную текст из второго элемента
    x3 = int(x1) + int(x2) #перевел каждый текстовый элемент в число и сложил числа
    print(x1)
    print(x2)
    print(x3)
    #x4 = str(x3) #перевел сумму обратно в строку т.к. иначе не находит
    # можно эту строку сразу в значение x4 = str(x3) #перевел сумму обратно в строку т.к. иначе не находит
    #print(x4)
    #print(x4+x4)
    open_list = browser.find_element(By.XPATH, "//*[@id='dropdown']").click()
    #select = Select(browser.find_element_by_tag_name("select"))
    select = Select(browser.find_element(By.TAG_NAME,"select"))
    select.select_by_value(str(x3))
    # еще вариант
    #time.sleep(1)
    btn1 = browser.find_element(By.XPATH, "//*[@type='submit']").click()

    alert = browser.switch_to.alert
    xxx = (alert.text.split()[-1])
    print('\n', xxx)
finally:
    time.sleep(3)
    browser.quit()


##def captcha():
