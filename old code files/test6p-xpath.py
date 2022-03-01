import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# ЧТО ЕЩЕ? ВСЕ ДАННЫЕ В МАССИВ, ЛОКАТОРЫ В ПЕРЕМЕННЫЕ? СЧИТАТЬ АЛЕРТ, ВЫБРАТЬ ЛУЧШЕЕ ИЗ РЕШЕНИЙ

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.XPATH, "//input[@type='text'][@name='first_name']")
input1.send_keys("Ivan")
input2 = browser.find_element(By.XPATH, "//input[@name='last_name']")
input2.send_keys("Petrov")
input3 = browser.find_element(By.XPATH, "//input[contains(@class, 'city')]")
input3.send_keys("Smolensk")
input4 = browser.find_element(By.XPATH, "//input[@id='country']")
input4.send_keys("Russia")
button = browser.find_element(By.XPATH, "//button[text()='Submit']")
button.click()
# print(Alert(browser).text.split()[-1])
print('\n')
print(Alert(browser).text)
time.sleep(2)
print('\n')
print('YES!!!! YOU ARE HERO!!!! NOW YOU KNOW XPATH VERY WELL ! ! ! ! !\n')
browser.quit()


# ========================ЧЕРНОВИК ЗДЕСЬ =========================

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# # ПРИЧИНА НАЙДЕНА - ОНА В БУКВE S - ELEMENTS OR ELEMENT !!!!!!!!!!!!!!!!!!!
# # input1 = browser.find_element_by_xpath('//input[@type="text"][@name="first_name"]')
# # input1 = browser.find_elements_by_xpath("//input")[0]
# # input1 = browser.find_element(By.XPATH, "//input")
# input1 = browser.find_element(By.XPATH, "//input[@type='text'][@name='first_name']")
# input1.send_keys("Ivan")
# #input2 = browser.find_elements_by_xpath("//input")[1]
# input2 = browser.find_element(By.XPATH, "//input[@name='last_name']")
# input2.send_keys("Petrov")
# #input3 = browser.find_elements_by_xpath("//input")[2]
# input3 = browser.find_element(By.XPATH, "//input[contains(@class, 'city')]")
# input3.send_keys("Smolensk")
# #input4 = browser.find_elements_by_xpath("//input")[3]
# input4 = browser.find_element(By.XPATH, "//input[@id='country']")
# input4.send_keys("Russia")
# #button = browser.find_element_by_css_selector("button.btn")
# button = browser.find_element(By.XPATH, "//button[text()='Submit']")
# button.click()
# time.sleep(5)
# #print('line1\nline2')
# print('\n')
# print('YES!!!! YOU ARE HERO!!!! NOW YOU KNOW XPATH VERY WELL ! ! ! ! !\n')
# browser.quit()




# =================================================

# import time
# from selenium import webdriver
#
# def working():
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome()
#     driver.get('http://suninjuly.github.io/simple_form_find_task.html')
#
#     try:
#         input1 = driver.find_element_by_name('first_name')
#         input1.send_keys("Ivan")
#         input2 = driver.find_element_by_name('last_name')
#         input2.send_keys("Petrov")
#         input3 = driver.find_element_by_xpath('//input[@class="form-control city"]')
#         input3.send_keys("Smolensk")
#         input4 = driver.find_element_by_id('country')
#         input4.send_keys("Russia")
#         button = driver.find_element_by_css_selector("button.btn")
#         button.click()
#         time.sleep(100)
#
#     except Exception as errors:
#         print(f'Ошибка в глобальном скоупе | {errors}')
#
#     finally:
#         driver.close()
#         sleep(2)
#         driver.quit()
#
# working()
#

# ПОКА НЕ РАЗОБРАЛСЯ КАК ПИШЕТСЯ НОВЫЙ СИНТАКСИС =ХПАФ!!!!
# ПРИЧИНА НАЙДЕНА - ОНА В БУКВE S - ELEMENTS OR ELEMENT
# from selenium import webdriver
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# # ПРИЧИНА НАЙДЕНА - ОНА В БУКВE S - ELEMENTS OR ELEMENT !!!!!!!!!!!!!!!!!!!
# input1 = browser.find_element_by_xpath('//input[@type="text"][@name="first_name"]')
# #input1 = browser.find_elements_by_xpath("//input")[0]
# input1.send_keys("Ivan")
# input2 = browser.find_elements_by_xpath("//input")[1]
# input2.send_keys("Petrov")
# input3 = browser.find_elements_by_xpath("//input")[2]
# input3.send_keys("Smolensk")
# input4 = browser.find_elements_by_xpath("//input")[3]
# input4.send_keys("Russia")
# button = browser.find_element_by_css_selector("button.btn")
# button.click()

#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#   #  input1 = browser.find_element_by_xpath('//input[@type="text"][@name="first_name"]')
# input1 = browser.find_element(By.XPATH '//input[@type="text"][@name="first_name"]')
#    #   input1 = browser.find_element_by_xpath('//input[@name="first_name"]')
#    # input1 = browser.find_element_by_tag_name("first_name")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_css_selector(".city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#    time.sleep(5)
#     # закрываем браузер после всех манипуляций
# browser.quit()

