from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'

try:
    browser.get(link)
    f_name = browser.find_element(By.XPATH, "//*[@name='firstname']").send_keys('ROBOT')
    l_name = browser.find_element(By.XPATH, "//*[@name='lastname']").send_keys('ANDROID')
    email = browser.find_element(By.XPATH, "//*[@name='email']").send_keys('BOSS@GOOGLE.COM')
    send_file = browser.find_element(By.XPATH, "//*[@type='file']").send_keys('C:/Users/user41/PycharmProjects/pythonProject-28-12-2021/test-file-for-lesson.txt')
    click_btn = browser.find_element(By.XPATH, "//*[@type='submit']").click()
    print(browser.switch_to.alert.text)
    # попробую опцию создать файл !!!!! РАБОТАЕТ!!! ЭТА КОМАНДА СОЗДАЕТ ФАЙЛ!!!!! КЛАСС!!!
    #with open("test123-test.txt", "w") as file:
    #    content = file.write("automationbypython")  # create test.txt file

finally:
    time.sleep(5)
    #browser.quit()