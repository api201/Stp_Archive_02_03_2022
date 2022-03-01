from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


link = "http://suninjuly.github.io/registration2.html"

try:
  #  s = Service('Тут должен быть адрес до chromedriver')
    #driver = webdriver.Chrome(service=s)
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(link)

    input1 = driver.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.XPATH, "//*[normalize-space(.)=\"Last name*\"]/input")
    input2.send_keys("Petrov")
#    input3 = driver.find_element_by_class_name("form-control_third")
#    input3.send_keys("Smolensk")
 #   input4 = driver.find_element_by_id("country")
  #  input4.send_keys("Russia")
    input3 = driver.find_element(By.XPATH, "//*[normalize-space(.)=\"Email*\"]/input").send_keys("test@test.ru")
    button = driver.find_element(By.XPATH, "//*[normalize-space(.)=\"Submit\"]")
    button.click()

   # button = driver.find_element_by_css_selector("button.btn")
    #button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла