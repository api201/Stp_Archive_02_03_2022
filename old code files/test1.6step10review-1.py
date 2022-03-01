from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    link1 = 'http://suninjuly.github.io/registration1.html'
    link2 = 'http://suninjuly.github.io/registration2.html'
    browser.get(link1)

    #input1 = browser.find_element(By.XPATH, '//label[text()=\'First name*\']/following-sibling::input')
    #input1.send_keys('Anton')

    input1 = browser.find_element(By.XPATH, '//label[text()=\'First name*\']/following-sibling::input').send_keys('Anton')

    input2 = browser.find_element(By.XPATH, '//label[text()=\'Last name*\']/following-sibling::input')
    input2.send_keys('Fedorov')

    input3 = browser.find_element(By.XPATH, '//label[text()=\'Email*\']/following-sibling::input')
    input3.send_keys('af@gmail.com')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()