import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "submit_button")
time.sleep(2) #все работает, элемент находит
button.click()

# закрываем браузер после всех манипуляций
browser.quit()