from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")
xx = int(browser.find_element(By.ID,'input_value').text)
print(xx)
otwet = math.log(abs(12*math.sin(xx)))
print(otwet)
browser.execute_script("window.scrollTo(0, 99)")
send_answer = browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(otwet)
i_am_robot = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']").click()
robots_rule = browser.find_element(By.XPATH, "//*[@id='robotsRule']").click()
press_button = browser.find_element(By.XPATH, "//*[@type='submit']").click()
print(browser.switch_to.alert.text)


#x = ln(abs(12*sin(273)))
#x = (abs(12*sin(273)))
#x = math.log()log(abs(12*sin(273)))
#x = math.log(abs(12*math.sin(273)))
#print(x)

#finally:
    #time.sleep(3)
   # browser.quit()

