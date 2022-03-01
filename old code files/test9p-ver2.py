from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

try:
    link = 'http://suninjuly.github.io/find_xpath_form'
    browser = webdriver.Chrome()
    browser.get(link)

    #input_list = browser.find_elements_by_tag_name('input')
    input_list = browser.find_elements(By.TAG_NAME,'input')
    output_list = ['Sergey', 'Pushkin', 'Moscow', 'Russia']
    #submit = browser.find_element_by_xpath('//button[text()="Submit"]')
    #submit = browser.find_element(By.XPATH,'//button[text()="Submit"]')
    submit = browser.find_element(By.XPATH,'//button[@type=contains(.,"ubm")]') # ДАААААААА !!!!!!!!!!!!!!
    #count3 = len(browser.find_elements_by_tag_name('input'))
    count3 = len(browser.find_elements(By.TAG_NAME,'input'))
    #print('\n')
    #print('============== Количество найденных элементов = ', count3)

    print('\n''============== Количество найденных элементов = ', count3,'\n')
    #print('\n', input_list)

    for el, data in zip(input_list, output_list):
        el.send_keys(data)
    submit.click()

finally:
    sleep(3)
    browser.quit()



############################ вариант с циклом

# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
#
# try:
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/find_xpath_form"
#     browser.get(link)
#     fields = browser.find_elements(By.CSS_SELECTOR, '[type="text"]')
#
#     for field in fields:
#         field.send_keys("test")
#
#     submit = browser.find_element(By.XPATH, '//div[6]/button[3]').click()
#
# finally:
#     sleep(3)
#     browser.quit()