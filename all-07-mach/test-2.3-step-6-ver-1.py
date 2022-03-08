from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser.get(link)
    #new_w = browser.switch_to.window('Redirect page')
    #browser.switch_to.window('Redirect page')
    press_button = browser.find_element(By.XPATH, "//*[@type='submit']").click()
    time.sleep(1)
    first_window = browser.window_handles[0]
    print(first_window)
    sw = browser.window_handles[1]
    print(sw)
    browser.switch_to.window(sw)
    #browser.switch_to.window('Redirect page')

    xx = int(browser.find_element(By.ID, 'input_value').text)
    print(xx)
    otwet = math.log(abs(12 * math.sin(xx)))
    send_answer = browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(otwet)
    press_button2 = browser.find_element(By.XPATH, "//*[@type='submit']").click()



    #new_window = 'http://suninjuly.github.io/redirect_page.html'
    #browser.switch_to.window(new_window)
    #browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")

    #button1 = browser.find_element(By.XPATH, "//button[@type='submit']").click()
    # alert = browser.switch_to.alert
    # time.sleep(2)
    # alert.accept()
    #
    # xx = int(browser.find_element(By.ID, 'input_value').text)
    # print(xx)
    # otwet = math.log(abs(12 * math.sin(xx)))
    # browser.execute_script("window.scrollTo(0, 99)")
    # send_answer = browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(otwet)
    # press_button = browser.find_element(By.XPATH, "//*[@type='submit']").click()
    # print(browser.switch_to.alert.text)



finally:
    time.sleep(3)
    #browser.quit()