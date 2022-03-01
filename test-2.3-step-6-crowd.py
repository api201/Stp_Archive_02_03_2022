from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
#browser.get('http://suninjuly.github.io/redirect_accept.html')
#link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    press_button = browser.find_element(By.XPATH, "//*[@type='submit']").click()
    browser.switch_to.window(browser.window_handles[1])
    xx = int(browser.find_element(By.ID, 'input_value').text)
    otwet = math.log(abs(12 * math.sin(xx)))
    send_answer = browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(otwet)
    press_button2 = browser.find_element(By.XPATH, "//*[@type='submit']").click()

finally:
    time.sleep(3)
    #browser.quit()