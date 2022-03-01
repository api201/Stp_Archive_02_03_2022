import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import math

try:
    browser = webdriver.Chrome()
    url = "http://suninjuly.github.io/find_link_text"
    browser.get(url)
  #  str(math.ceil(math.pow(math.pi, math.e) * 10000)) - это лишняя строка
    #link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e) * 10000)))
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000)))
    #_by_link_text(str(math.ceil(math.pow(math.pi, math.e) * 10000)))
    link.click()

    first_n = browser.find_element(By.XPATH, "//*[@type='text'][@name='first_name']").send_keys("VLAD _ _ NAME") # * instead input tag
    # first_n = browser.find_element(By.XPATH, "//input[@type='text'][@name='first_name']").send_keys("VLAD _ _ NAME")
    second_n = browser.find_element(By.CSS_SELECTOR, "input[name='last_name']").send_keys("SELENIUM TEST")
    city = browser.find_element(By.CLASS_NAME, "city").send_keys("RIGA")
    country = browser.find_element(By.ID, "country").send_keys("EUROPE IS MY HOME")
    push_submit = browser.find_element(By.XPATH, "//button[text()='Submit']")
    push_submit.click()
    # print('\n =========================================== TEST 1 STARTED =============================================')
    # print('\n')
    # print(Alert(browser).text)
    print('\n')
    print('                               YOUR TEST PASSED SUCCESSFULLY! YOU ARE GOOD :) \n')

except:
    print('\n ERROR! TEST FAILED!')
finally:
  time.sleep(2)
  browser.quit()

