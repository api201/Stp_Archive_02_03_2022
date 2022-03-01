from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    #browser.get("http://suninjuly.github.io/selects2.html")
    find_x1 = browser.find_element(By.ID, "num1")
    find_x2 = browser.find_element(By.XPATH, "//*[@id='num2']")
    x1 = find_x1.text
    x2 = find_x2.text
    x3 = int(x1) + int(x2)
    print(x1)
    print(x2)
    print('\n')
    print(x3)
    x4 = str(x3)
    #print(x4+x4)  #test-2.2-step-3-ver-1
    # print(find_x1)
    x5 = str(int(x1)+int(x2))
    print(x5)
    #ww = str('13')
    #z = value("98")

    open_list = browser.find_element(By.XPATH, "//*[@id='dropdown']").click()
    #time.sleep(1)
    #send_answer = browser.find_element(By.XPATH, "//option[@value=x4]")
    #send_answer = browser.find_element(By.XPATH, "//option[@value=ww]")
    #send_answer = browser.find_element(By.XPATH, "//option[text()=ww]")
    #send_answer = browser.find_element(By.XPATH, "//option[text()=ww]")
    #send_answer = browser.find_element(By.XPATH, "//option[@value=x5]").click()

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(x4)

    btn1 = browser.find_element(By.XPATH, "//*[@type='submit']").click()

   # browser.find_element(By.CSS_SELECTOR, x3).click()


  #   y = calc(x)
  #   #z = str(math.log(abs(12*math.sin(int(x)))))
  #   print(y)
  #   print('\n')
  #   #print(z)
  #
  #   send_answer = browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)
  #   time.sleep(1)
  #   robot_box = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
  #   time.sleep(1)
  #   robots_rule = browser.find_element(By.XPATH, "//label[@for='robotsRule']").click()
  #   time.sleep(1)
  #   submit_btn = browser.find_element(By.XPATH, "//button[@type='submit']").click()
  #
  # #ДОБАВЬ ЕЩЕ КОД НА СЧИТЫВАНИЕ АЛЕРТА И ПРОСМОТРИ РЕШЕНИЯ ДРУГИХ РЕБЯТ

finally:
    time.sleep(3)
   # browser.quit()


##def captcha():
