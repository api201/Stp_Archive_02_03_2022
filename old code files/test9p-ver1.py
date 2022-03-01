from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    input0 = browser.find_element(By.XPATH, '//*[@name="first_name"]').send_keys("TEST-NAME")
    input1 = browser.find_element(By.XPATH, '//*[@name="last_name"]').send_keys("FFFFFFFFF")
    input2 = browser.find_element(By.XPATH, '//*[@name="firstname"]').send_keys("LONDON")
    #input3 = browser.find_element_by_xpath('//input[@class="form-control city"]')
    input3 = browser.find_element(By.XPATH, '//*[@id="country"]').send_keys("AFRIKA")
    #btn = browser.find_element(By.XPATH, '//*[@type="submit"]').click()
    #btn = browser.find_element(By.XPATH, '//button[text()="Submit1"]').click()
    #button = browser.find_elements_by_xpath("//button[@type='submit']")[0].click()
    #button = browser.find_element_by_xpath("//button[contains(text(), 'Subm')]").click() #регистр важен 'subm' например не сработает
    #button = browser.find_elements_by_xpath("//button[@type='submit']").click() #не работает без [0]
    # buttons = browser.find_elements_by_xpath("//button")
    # for button in buttons:
    #     if button.text == 'Submit':
    #         button.click()
    #         break
    #btn = browser.find_element(By.XPATH, '//*[@type contains(text(), "ubm")]').click()
    #btn = browser.find_element(By.XPATH, '//button[@type, "submit" and text() = "Submit")]').click()
    btn = browser.find_element(By.XPATH, '//button[@type=contains(., "ubm")]').click()


#except Exception as e:
 #     print(e)

finally:
   time.sleep(3)
   browser.quit()



