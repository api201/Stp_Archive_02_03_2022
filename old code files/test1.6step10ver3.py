from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    url = 'http://suninjuly.github.io/registration1.html'
    browser.get(url)

    # Ваш код, который заполняет обязательные поля
    required_elements = browser.find_elements_by_css_selector('input[required]')
    for element in required_elements:
        element.send_keys('required')
    time.sleep(3)
    submit = browser.find_element_by_tag_name('button')
    submit.click()

    time.sleep(1)
    welcome_text = browser.find_element_by_tag_name('h1').text
    assert 'Congratulations' in welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()