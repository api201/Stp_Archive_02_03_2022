from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("BILL")
    second_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("GATES")
    send_email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("BILL_GATES@WINDOWS.COM")
    phone = browser.find_element(By.XPATH, "//*[normalize-space(.)='Phone:']/input").send_keys("+7-495-444-55555")
    adress = browser.find_element(By.XPATH, "//label[text()=\'Address:\']/following-sibling::input").send_keys("LONDON")
    time.sleep(4)
    submit_btn = browser.find_element(By.XPATH, "//*[text()='Submit']").click()

    # Отправляем заполненную форму
    #button = browser.find_element_by_css_selector("button.btn")
    #button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()