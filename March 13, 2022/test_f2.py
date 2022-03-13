import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()
link = f"https://stepik.org/lesson/236895/step/1"
browser.get(link)
time.sleep(3)
#find_x = browser.find_element(By.XPATH, "//*[@id='ember85']").send_keys("12344")
answer = math.log(int(time.time()))
#find_x = browser.find_element(By.XPATH, "//*[@placeholder='Type your answer here...']").send_keys("12344")
find_x = browser.find_element(By.XPATH, "//*[@placeholder='Type your answer here...']").send_keys(answer)
logInBtn = browser.find_element(By.XPATH, "//*[@class='submit-submission']").click()
time.sleep(3)