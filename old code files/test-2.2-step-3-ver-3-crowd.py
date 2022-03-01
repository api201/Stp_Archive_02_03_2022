########################################## версия 8 -  еще

from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

# ссылка на стартовую страницу


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    # находим сумму
    sum_for_search = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(sum_for_search))
    browser.find_element_by_tag_name('button').click()
    print(browser.switch_to.alert.text)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

########################################## версия 7 -  select.select_by_value(str(s))

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
#
# link = "http://suninjuly.github.io/selects1.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
#
# n1 = browser.find_element_by_id("num1")
# n2 = browser.find_element_by_id("num2")
#
# x = n1.text
# y = n2.text
# s = int(x) + int(y)
#
# select = Select(browser.find_element_by_tag_name("select"))
# select.select_by_value(str(s)) ###### СРАЗУ ПЕРЕВОДИМ В СТРОКУ
#
#
# button = browser.find_element_by_class_name("btn.btn-default")  ######### ПОИСК ПО ИМЕНИ КЛАССА
# button.click()



########################################## версия 6 - еще вариант

# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support.ui import Select
#
# # Открыть браузер
# con = WebDriver()
#
# # Открыть страницу http://suninjuly.github.io/selects1.html
# con.get("http://suninjuly.github.io/selects1.html")
#
# # Найти веб-элементы с числами, выпадающим списком и кнопкой
# first_num_el = con.find_element_by_css_selector("#num1")
# second_num_el = con.find_element_by_css_selector("#num2")
#
# drop_list = Select(con.find_element_by_css_selector("select"))
#
# submit_btn = con.find_element_by_css_selector("[type='submit']")
#
# # Посчитать сумму заданных чисел
# sum = int(first_num_el.text) + int(second_num_el.text)
#
# # Выбрать в выпадающем списке значение равное расчитанной сумме
# drop_list.select_by_visible_text(str(sum))
#
# # Нажать кнопку "Отправить"
# submit_btn.click()



########################################## версия 5 - РЕШАЕМ ЧЕРЕЗ ЦИКЛ

# from selenium import webdriver
#
# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/selects1.html"
# browser.get(link)
#
# try:
#     x = browser.find_element_by_css_selector("#num1").text
#     y = browser.find_element_by_css_selector("#num2").text
#     summ = int(x) + int(y)
#
#     elements = browser.find_elements_by_css_selector("#dropdown option") # КРУТАААА!!!!! ЦИКЛ!!!!
#     for element in elements:
#         select_num = element.get_attribute("value")
#         if select_num.isdigit() and int(select_num) == summ:
#         #if int(select_num) == summ: - так не работает
#             element.click()
#             break
#
#     browser.find_element_by_css_selector("form button[type=submit]").click()
#
#     alert = browser.switch_to.alert
#     print(alert.text) # КРУТО !!!!!!!!!! ПЕЧАТАЕМ ВЕСЬ АЛЕРТ !!!!!!!!!!
#     alert.accept()
#     browser.close()
#
# finally:
#     browser.quit()


########################################## версия 4 - КОРОТКИЙ КОД

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# link = "http://suninjuly.github.io/selects1.html"
# b = webdriver.Chrome()
# b.get(link)
#
# num1 = b.find_element_by_css_selector("#num1").text
# num2 = b.find_element_by_css_selector("#num2").text
# sm = str(int(num1) + int(num2))
# print(sm)
#
# select = Select(b.find_element_by_css_selector("#dropdown"))
# select.select_by_value(sm)
# b.find_element_by_css_selector(".btn").click()
#
# print(b.switch_to.alert.text.split()[-1]) # Я ДОБАВИЛ СТРОЧКУ ВЫВОДА АЛЕРТА - ОТЛИЧНО РАБОТАЕТ !!!!!!!!!!


########################################## версия 3 - КРУТО С WITH И АЛЕРТ В ОДНУ СТРОКУ !!!!!!!!!!!! + НИКАКИХ ВЫХОДОВ И TRY

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# url = 'http://suninjuly.github.io/selects2.html'
#
# with webdriver.Chrome() as b:
#     #     Открываем страницу в браузере
#     b.get(url)
#
#     #     Находим все цИфры в строке и добавляем их в список
#     numb_list = [int(i.text) for i in
#                  b.find_elements_by_css_selector('h2 .nowrap')
#                  if i.text.isdecimal()]
#
#     #     открываем выпадающий список
#     #     b.find_element_by_id('dropdown').click()
#     select = Select(b.find_element_by_tag_name('select'))
#
#     #     ищем ответ в списке и выбираем его
#     #     b.find_element_by_css_selector(f'[value = "{sum(numb_list)}"]').click()
#     select.select_by_value(f'{sum(numb_list)}')
#
#     #     находим кнопку и жмакаем
#     b.find_element_by_class_name('btn').click()
#
#     #     ловим алерт и забираем из него ответ
#     print(b.switch_to.alert.text.split()[-1])

########################################## версия 2 - функция суммы отдельно

# from selenium import webdriver
# import time
# import math
#
# def calc(x, y):
#     return str(int(x) + int(y))
#
# try:
#     link = "http://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     x_element = browser.find_element_by_css_selector("#num1")
#     x = x_element.text
#     y_element = browser.find_element_by_css_selector("#num2")
#     y = y_element.text
#     z = calc(x, y)
#     print(z+z) # МОЯ ПРОВЕРКА ПОКАЗЫВАЕТ ТИП СЛОЖЕНИЯ НАПРИМЕР ЕСЛИ 83, ТО РАВНО 8383, А НЕ СУММА 83+83
#     element = browser.find_element_by_id("dropdown").click()
#     browser.find_element_by_css_selector("[value='" + z + "']").click()
#
#     tap = browser.find_element_by_css_selector("button").click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

########################################## версия 1 - короткая запись
# from selenium import webdriver
# import time
# from selenium.webdriver.support.ui import Select
#
# link = "http://suninjuly.github.io/selects1.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# try:
#
#     sum1 = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)
#
#     select = Select(browser.find_element_by_css_selector("select"))
#     select.select_by_value(str(sum1))
#
#     button = browser.find_element_by_tag_name(".btn").click()
#
#
# except Exception as error:
#     print(f'Произошла ошибка, вот её трэйсбэк: {error}')
#
# finally:
#
#     time.sleep(4)
#
#     #browser.close()
#     browser.quit()