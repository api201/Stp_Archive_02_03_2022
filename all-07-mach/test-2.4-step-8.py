from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
        #EC.element_to_be_clickable((By.ID, "verify"))
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
button_book = browser.find_element(By.ID, "book").click()

xx = int(browser.find_element(By.ID, 'input_value').text)
print(xx)
otwet = math.log(abs(12 * math.sin(xx)))
send_answer = browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(otwet)
press_button2 = browser.find_element(By.XPATH, "//*[@type='submit']").click()

#message = browser.find_element_by_id("verify_message")

#assert "successful" in message.text


