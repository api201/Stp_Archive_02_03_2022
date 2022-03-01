############## ВАРИАНТ 4  - ПЕЧАТАЕТ ОТВЕТ #####################

import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/math.html"
browser.get(link)

try:
    x_element = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(calc(x_element))
    elements_to_select = tuple(("[id = 'robotCheckbox']", "[for=\"robotsRule\"]", "button.btn.btn-default"))

    for elem in elements_to_select:
        browser.find_element_by_css_selector(elem).click()

    print_answer(browser)
finally:
    browser.quit()


############## ВАРИАНТ 3 - САМЫЙ КОРОТКИЙ #####################

# from selenium import webdriver
# from math import log, sin
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/math.html")
#
# x = browser.find_element_by_css_selector('[id = "input_value"]').text
# browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12 * sin(int(x))))))
#
# for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
#     browser.find_element_by_css_selector(selector).click()