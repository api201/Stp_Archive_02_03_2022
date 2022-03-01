
# ================ ТРИ ФУНКЦИИ ====================

from selenium import webdriver
import time
import math

def working():
    driver = webdriver.Chrome()

    try:
        def login():
            driver.find_element_by_name('first_name').send_keys("Ivan")
            driver.find_element_by_name('last_name').send_keys("Petrov")
            driver.find_element_by_xpath('//input[@class="form-control city"]').send_keys("Smolensk")
            driver.find_element_by_id('country').send_keys("Russia")
            driver.find_element_by_css_selector("button.btn").click()
            time.sleep(2)

        def go_page():
            driver.get('http://suninjuly.github.io/find_link_text')
            time.sleep(1)
            driver.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000))).click()

        go_page()
        login()

    except Exception as errors:
        print(f'Ошибка в глобальном скоупе | {errors}')

    finally:
       # driver.close()
        time.sleep(1)
        driver.quit()

working()

# ПРИКОЛЬНО!!!! АЛЕРТ НЕ ВЫВОДИТСЯ, НО ВЫПОЛНЯЕТСЯ ПРОВЕРКА АЛЕРТА И ПОТОМ ОН ПЕЧАТАЕТСЯ В КОНСОЛИ

# import math
#
# from selenium import webdriver
#
# secret_link: str = str(math.ceil(math.pow(math.pi, math.e)*10000))
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/find_link_text")
# link = browser.find_element_by_link_text(secret_link)
# link.click()
#
# input1 = browser.find_element_by_tag_name("input")
# input1.send_keys("Ivan")
# input2 = browser.find_element_by_name("last_name")
# input2.send_keys("Petrov")
# input3 = browser.find_element_by_class_name("city")
# input3.send_keys("Smolensk")
# input4 = browser.find_element_by_id("country")
# input4.send_keys("Russia")
# button = browser.find_element_by_css_selector("button.btn")
# button.click()
#
# alert = browser.switch_to.alert
# alert_text = alert.text
# # validate the alert text
# alert.accept()
#
# print(alert_text.split()[-1])
#
# browser.close()
# browser.quit()





# ============ browser.switch_to.alert.text ===========================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math
# import time
#
# page = "http://suninjuly.github.io/find_link_text"
#
# with webdriver.Chrome() as browser:
#     browser.get(page)
#     link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
#     link.click()
#
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
#
#     answer = browser.switch_to.alert.text
#     print(answer)
#     time.sleep(3)
#     browser.quit()


# ============ except Exception() as e: ===========================
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/find_link_text')
#     text = str(math.ceil(math.pow(math.pi, math.e)*10000))
#     link = browser.find_element_by_link_text(text)
#     link.click()
#
#     first_name = browser.find_element_by_name('first_name')
#     last_name = browser.find_element_by_name('last_name')
#     city = browser.find_element_by_css_selector('.city')
#     country = browser.find_element_by_id('country')
#     submit = browser.find_element_by_tag_name('button')
#
#     first_name.send_keys('Alexey')
#     last_name.send_keys('Prohorov')
#     city.send_keys('Moscow')
#     country.send_keys('Bootovo')
#     submit.click()
# except Exception() as e:
#     print(e)
# finally:
#     a = str(math.ceil(math.pow(math.pi, math.e) * 10000))
#     print(a)
#     time.sleep(3)
#     browser.quit()


# from selenium import webdriver
# import math
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
#
# # ============ ПРИМЕР С НОРМАЛЬНЫМИ ОЖИДАНИЯМИ ===========================
#
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('http://suninjuly.github.io/find_link_text')
# searching_element = str(math.ceil(math.pow(math.pi, math.e) * 10000))
# try:
#     browser.find_element_by_link_text(searching_element).click()
#     browser.find_element_by_name('first_name').send_keys('name')
#     browser.find_element_by_name('last_name').send_keys('soname')
#     browser.find_element_by_name('firstname').send_keys('city_of_stars')
#     browser.find_element(By.ID, 'country').send_keys('RUSSIA')
#     browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
#     alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
#     print(alert.text)
#
# finally:
#     sleep(3)
#     browser.quit()
#
# # C ожиданиями и вывоводом результата в консоль пайчарма