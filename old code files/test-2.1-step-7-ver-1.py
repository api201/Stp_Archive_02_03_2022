from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    find_treasure = browser.find_element(By.ID, "treasure")
    value_of_treasure = find_treasure.get_attribute("valuex")
    print(value_of_treasure)

    otwet = calc(value_of_treasure)
    print(otwet)

    send_answer = browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(otwet)
    time.sleep(1)
    robot_box = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
    time.sleep(1)
    robots_rule = browser.find_element(By.XPATH, "//input[@id='robotsRule']").click()
    time.sleep(1)
    submit_btn = browser.find_element(By.XPATH, "//button[@type='submit']").click()

    alert = browser.switch_to.alert
    xxx = (alert.text.split()[-1])
    print('\n',xxx)

finally:
    time.sleep(3)
   # browser.quit()


