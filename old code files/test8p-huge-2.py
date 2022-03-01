

# ===================== ВАРИАНТ 5 - рандомные предложения

# from selenium import webdriver
# import time, random
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements_by_tag_name("input")
#     for element in elements:
#         A = random.sample(list("AVHHTCVRESEWTYUJOLKLJ"), 1)
#         B = random.sample(list("aaaaaqwrtooooooyuiooopsdfghjuuuuklzxcvbeeeeeeeenm"), random.randint(5, 30))
#         C = ''.join(A + B).replace("u", ' ')
#         element.send_keys(C)
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# ===================== ВАРИАНТ 4 - еще с РАНДОМ с функциями

# import random
# from selenium import webdriver
#
# link = "http://suninjuly.github.io/huge_form.html"
# letters = list(range(97, 123)) + list(range(65, 91))
#
# browser = webdriver.Chrome()
# browser.get(link)
#
# try:
#     for element in browser.find_elements_by_css_selector("input[type=text]"):
#         element.send_keys("".join(map(chr, random.sample(letters, random.randint(3, 15)))))
#
#     button = browser.find_element_by_css_selector("form[method=get] button[type=submit]")
#     button.click()
#
#     alert = browser.switch_to.alert
#     print(alert.text)
#     alert.accept()
#     browser.close()
#
# finally:
#     browser.quit()


# # ===================== ВАРИАНТ 3 с функциями
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def fill_forms(driver, by, value, answer):
#     """Заполняет формы"""
#     elements = driver.find_elements(by, value)
#     for element in elements:
#         element.send_keys(answer)
#
# def click_submit(driver, by, value):
#     """Отправляет GET запрос"""
#     button_submit = driver.find_element(by, value)
#     button_submit.click()
#
# def get_key(driver):
#     """Распечатывает код ответа"""
#     alert = driver.switch_to.alert
#     answer = alert.text.split()[-1]
#     print(answer)
#
# def main(url):
#     import time
#
#     try:
#         browser = webdriver.Chrome()
#         browser.get(url)
#
#         fill_forms(driver=browser, by=By.TAG_NAME, value='input', answer='Ok')
#         click_submit(driver=browser, by=By.CSS_SELECTOR, value='button.btn')
#         get_key(driver=browser)
#     except Exception as err:
#         print(f'Ошибка: {err}')
#     finally:
#         time.sleep(10)
#         browser.quit()
#
#
# if __name__ == '__main__':
#     url = 'http://suninjuly.github.io/huge_form.html'
#     main(url)


# # ===================== ВАРИАНТ 2  #СУПЕР! ЗАПОЛНЯЕМ РАНДОМНЫМИ СИМВОЛАМИ!!!
# from selenium import webdriver
# import time
# import random
# import string
#
# try:
#
#     options = webdriver.ChromeOptions()
#
#     options.add_experimental_option("excludeSwitches", ["enable-logging"])
#
#     browser = webdriver.Chrome(options=options)
#
#     # подавление ошибки юсб ERROR:device_event_log_impl.cc(214)
#
#     #  USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection:
#
#     browser.get('http://suninjuly.github.io/huge_form.html')
#
#     elements = browser.find_elements_by_tag_name('input')
#
#     for element in elements:
#         element.send_keys(''.join(random.choice(string.ascii_lowercase) for _ in range(15)))
#
#         # заполняем поле  случайными 8 буквами
#
#     time.sleep(3)
#
#     button = browser.find_element_by_xpath('//button')
#
#     button.click()
#
# finally:
#
#     #alert = browser.switch_to_alert()  # ошибка??? не нужны скобки???
#     alert = browser.switch_to.alert  # !!!!!!!!!! ПРАВИЛЬНО С ТОЧКОЙ И БЕЗ СКОБОК
#
#     print('---------------------------------\n\n\n\n', alert.text)  # выводим его в консоль
#
#     # успеваем скопировать код за 30 секунд
#
#     # time.sleep(30)
#
#     # закрываем браузер после всех манипуляций
#
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла


# ===================== ВАРИАНТ 1  #СУПЕР! С НОВЫМ МЕТОДОМ!!!

# from selenium import webdriver
# import time
#
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/huge_form.html"
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     elements = browser.find_elements(By.CSS_SELECTOR, '[type=text]') #СУПЕР! С НОВЫМ МЕТОДОМ!!!
#     for element in elements:
#         element.send_keys('My response')
#
#     button = browser.find_element(By.CLASS_NAME, 'btn')
#     button.click()
#
# except:
#     time.sleep(30)
#     browser.quit()