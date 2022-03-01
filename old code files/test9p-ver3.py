import random
from selenium import webdriver
from time import sleep

link = "http://suninjuly.github.io/find_xpath_form"
letters = list(range(97, 123)) + list(range(65, 91))

browser = webdriver.Chrome()
browser.get(link)

try:
    for element in browser.find_elements_by_css_selector("input[type=text]"):
        element.send_keys("".join(map(chr, random.sample(letters, random.randint(3, 15))))) #КРУТОЙ РАНДОМ

    button = browser.find_element_by_css_selector("form[method=get] button[type=submit]") #КРУТОЙ ПОИСК ПО CSS
    button.click()

    alert = browser.switch_to.alert #КРУТО ПЕРЕКЛЮЧИЛ НА АЛЕРТЫ
    print(alert.text) #КРУТО НАПЕЧАТАЛ АЛЕРТ
    sleep(3)
    alert.accept()
    browser.close()

finally:
    browser.quit()