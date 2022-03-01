from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
###################################### Версия 2.2 - с выводом алерта в консоль и залогиниться на степике

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    find_x = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = find_x.text
    print(x)
    print('\n')

    y = calc(x)
    #z = str(math.log(abs(12*math.sin(int(x)))))
    print(y)
    print('\n')
    #print(z)

    send_answer = browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)
    time.sleep(1)
    robot_box = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
    time.sleep(1)
    robots_rule = browser.find_element(By.XPATH, "//label[@for='robotsRule']").click()
    time.sleep(1)
    submit_btn = browser.find_element(By.XPATH, "//button[@type='submit']").click()

    #print_answer(browser)
    #aa = print_answer(browser)
    #print(aa)
    alert = browser.switch_to.alert
    xxx = (alert.text.split()[-1])
    print(xxx)

    #answer = browser.switch_to.alert.text
    #print(answer)
    #alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    #print(alert.text)
    #print(Alert(browser).text)
    #print('\n')
    #print(Alert(browser).text)
    #print(Alert(browser).text)
    #otwet = (Alert(browser).text)
    #print(otwet)

  #ДОБАВЬ ЕЩЕ КОД НА СЧИТЫВАНИЕ АЛЕРТА И ПРОСМОТРИ РЕШЕНИЯ ДРУГИХ РЕБЯТ

    browser2 = webdriver.Chrome()
    browser2.maximize_window()
    #РЕГИСТРАЦИЯ НА СТЕПИКЕ УСПЕШНО!
    browser2.get("https://stepik.org/catalog")
    time.sleep(1)
    logInStepik = browser2.find_element(By.XPATH, "//*[text()='Log in']").click()
    time.sleep(1)
    logInEmail = browser2.find_element(By.XPATH, "//*[@name='login']").send_keys("vtest50@outlook.com")
    logInPass = browser2.find_element(By.XPATH, "//*[@name='password']").send_keys("vtest50@outlook.com")
    logInBtn = browser2.find_element(By.XPATH, "//*[@type='submit']").click()
    time.sleep(3)
    browser2.get("https://stepik.org/lesson/165493/step/5?unit=140087")
    #solveAgain = browser2.find_element(By.XPATH, "//button[text()='Solve again']").click()
    time.sleep(3)
    findH3 = browser2.find_element(By.XPATH, '//h3[text()="Write text answer"]')
    print("\n ============ H3 IS FOUND ===============")
    time.sleep(3)
    sendAnswer2Stepik = browser2.find_element(By.XPATH, "//*[@placeholder='Type your answer here...']").send_keys(xxx)
    time.sleep(2)
    answerBtn = browser2.find_element(By.XPATH, "//button[@class='submit-submission']").click()
    time.sleep(3)
    #Я ЗАБЫЛ КАК ИЗ ЭТОЙ ФРАЗЫ ВЫДЕРНУТЬ САМИ ЦИФРЫ С ОТВЕТАМИ
    # Congrats, you've passed the task! Copy this code as the answer to Stepik quiz: 28.87226002577163

finally:
    time.sleep(3)
   # browser.quit()


##def captcha():
