from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    url = 'http://suninjuly.github.io/registration1.html'
    browser.get(url)

    xpath = "//label[contains(text(), '*')]/following-sibling::input"
    #КРУТО ЧТО ХПАФ НАХОДИТСЯ ПО ЗВЕЗДОЧКЕ И ЗАПИСАН В ОТДЕЛЬНУЮ ПЕРЕМЕННУЮ !!!
    input_list = browser.find_elements_by_xpath(xpath)
    output_list = ['first_name', 'Last_name', 'email'] #КРУТО ЧТО ДАННЫЕ В МАССИВЕ! ! !
    submit = browser.find_element_by_tag_name('button')

    for element, data in zip(input_list, output_list): #ЧТО-ТО КРУТОЕ НО ХЗ КАК ЭТО РАБОТАЕТ
        element.send_keys(data)
        time.sleep(2)
    submit.click()

    time.sleep(1)
    welcome_text = browser.find_element_by_tag_name('h1').text
    assert 'Congratulations' in welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()