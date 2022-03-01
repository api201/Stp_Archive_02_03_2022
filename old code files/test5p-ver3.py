
# =============== ЕЩЕ ВАРИАНТ ЧЕРЕЗ find_element_by_xpath('//input[@class="form-control city"]')

import time
from selenium import webdriver


def working():
    options = webdriver.ChromeOptions()
 #   driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
    driver = webdriver.Chrome()

    driver.get('http://suninjuly.github.io/simple_form_find_task.html')


    try:
        input1 = driver.find_element_by_name('first_name')
        input1.send_keys("Ivan")
        input2 = driver.find_element_by_name('last_name')
        input2.send_keys("Petrov")
        input3 = driver.find_element_by_xpath('//input[@class="form-control city"]')
        input3.send_keys("Smolensk")
        input4 = driver.find_element_by_id('country')
        input4.send_keys("Russia")
        button = driver.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(5)


    except Exception as errors:
        print(f'Ошибка в глобальном скоупе | {errors}')

    finally:
        driver.close()
        sleep(2)
        driver.quit()

working()


# __import__("math").log(int(__import__("time").time())*12)

# # ================= КРУТО!!! ВСЕ ЧЕРЕЗ ИКС-ПАСС
#
# from selenium import webdriver
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# input1 = browser.find_elements_by_xpath("//input")[0]
# input1.send_keys("Ivan")
# input2 = browser.find_elements_by_xpath("//input")[1]
# input2.send_keys("Petrov")
# input3 = browser.find_elements_by_xpath("//input")[2]
# input3.send_keys("Smolensk")
# input4 = browser.find_elements_by_xpath("//input")[3]
# input4.send_keys("Russia")
# button = browser.find_element_by_css_selector("button.btn")
# button.click()

# ================= КРУТО!!! НИЧЕГО НЕ МЕНЯЛ, ПРОСТО ПРИСВОИЛ ЗНАЧЕНИЯ ПЕРЕМЕННЫМ

# from selenium import webdriver
# import time
#
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# value1 = 'input'
# value2 = 'last_name'
# value3 = 'city'
# value4 = 'country'
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name(value1)
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name(value2)
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name(value3)
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id(value4)
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
# #    button = browser.find_elements_by_xpath('//button[id()="submit_button"]').click() не работает
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(7)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# не забываем оставить пустую строку в конце файла


# ================= НАКОНЕЦ-ТО СОВРЕМЕННЫЙ КОД ВМЕСТО СТАРЬЯ

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# with webdriver.Chrome() as browser:
#     browser.get(link)
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#     print("Ты молодец! С наступающим НГ! Новая работа ждет тебя!!!")
#     time.sleep(7)


# =============== С ЗАХОДОМ НА СТЕПИК И ПОПЫТКОЙ ВВЕСТИ РЕШЕНИЕ В ПОЛЕ ЗАДАНИЯ (ДРАЙВЕР ФАЙЕРФОКС)
#
# from selenium import webdriver
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# link_login = "https://stepik.org/"
# link_answer = "https://stepik.org/lesson/138920/step/4?unit=196194"
#
# try:
#     # get verification code
#    # browser = webdriver.Firefox()
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     first_name = "first_name"
#     last_name = "last_name"
#     city = "city"
#     country = "country"
#
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys(first_name)
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys(last_name)
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys(city)
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys(country)
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     alert = browser.switch_to.alert
#     text_alert = alert.text
#     answer_value = text_alert[(text_alert.index(': '))+2:]
#     time.sleep(5)
#     alert.accept()
#
#     # log in
#     browser.get(link_login)
#     time.sleep(5)
#
#     submit_button = browser.find_element_by_css_selector(".navbar__auth")
#     submit_button.click()
#
#     login_email = "vtest50@outlook.com"
#     login_password = "vtest50@outlook.com"
#
#     s_username = browser.find_element_by_id("id_login_email")
#     s_username.send_keys(login_email)
#
#     s_password = browser.find_element_by_id("id_login_password")
#     s_password.send_keys(login_password)
#
#     button = browser.find_element_by_css_selector(".sign-form__btn")
#     button.click()
#
#     time.sleep(5)
#
#     # input verification code in textarea
#     browser.get(link_answer)
#     time.sleep(5)
#
#     textarea = browser.find_element_by_css_selector(".textarea")
#     textarea.send_keys(answer_value)
#     time.sleep(5)
#
#     submit_button = browser.find_element_by_css_selector(".submit-submission")
#     submit_button.click()
#     time.sleep(5)
#
# finally:
#     time.sleep(1)
#     # close browser
#     browser.quit()



# =============== ЗАРАНЕЕ ВЫНОСИМ ВСЕ ЛОКАТОРЫ В ПЕРЕМЕННЫЕ + ИНФО ОБ ОШИБКЕ

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/simple_form_find_task.html')
#
#     first_name = browser.find_element_by_name('first_name')
#     last_name = browser.find_element_by_name('last_name')
#     city = browser.find_element_by_css_selector('.city')
#     country = browser.find_element_by_id('country')
#     submit = browser.find_element_by_id('submit_button')
#
#     first_name.send_keys('Alexey')
#     last_name.send_keys('Prohorov')
#     city.send_keys('Moscow')
#     country.send_keys('Bootovo')
#     submit.click()
# except:
#     print('Ошибка!!!')
# finally:
#     time.sleep(10)
#     browser.quit()

# ===============С парсингом алерта, что-бы не копировать число из браузера

# import time
# from selenium import webdriver
# from selenium.webdriver.common.alert import Alert
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name('input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name('last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name('city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id('country')
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     print(Alert(browser).text.split()[-1])
#
# finally:
#     time.sleep(5)
#     browser.quit()

# =====================================

# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# quiz_list = ['alex', 'lebovski', 'spb', 'russia']
# for i, e in enumerate(browser.find_elements_by_css_selector \
#                    ('input[type=text]:nth-child(2)')):
#     e.send_keys(quiz_list[i])
# button = browser.find_element_by_id("submit_button")
# button.click()

# =====================================

# import time
# from selenium import webdriver
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# browser = webdriver.Chrome()
# browser.get(link)
#
# try:
#     dict = (
#         {"css":"input[name='first_name']", "text":"Ivan"},
#         {"css":"input[name='last_name']", "text": "Petrov"},
#         {"css":".city", "text":"Smolensk"},
#         {"css":"#country", "text":"Russia"}
#     )
#
#     for element in dict:
#         textarea = browser.find_element_by_css_selector(element["css"])
#         textarea.send_keys(element["text"])
#
#     button = browser.find_element_by_css_selector("#submit_button")
#     button.click()
# finally:
#     time.sleep(30)
#     browser.quit()