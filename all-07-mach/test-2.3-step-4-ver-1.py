from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser.get(link)
    button1 = browser.find_element(By.XPATH, "//button[@type='submit']").click()
    alert = browser.switch_to.alert
    time.sleep(2)
    alert.accept()

    xx = int(browser.find_element(By.ID, 'input_value').text)
    print(xx)
    otwet = math.log(abs(12 * math.sin(xx)))
    browser.execute_script("window.scrollTo(0, 99)")
    send_answer = browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(otwet)
    press_button = browser.find_element(By.XPATH, "//*[@type='submit']").click()
    print(browser.switch_to.alert.text)

    ######## еще раз нажать ОК на алерте
    # alert = browser.switch_to.alert
    # time.sleep(2)
    # alert.accept()

finally:
    time.sleep(3)
    #browser.quit()