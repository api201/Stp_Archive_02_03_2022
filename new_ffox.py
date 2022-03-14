from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
#driver = webdriver.Firefox()
#driver = webdriver.Firefox(executable_path=r'C:\geckodriver05feb\geckodriver.exe')
#driver = webdriver.Firefox(executable_path=r'C:\geckodriver05feb\geckodriver.exe', options=options)

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\geckodriver05feb\geckodriver.exe', options=options)

driver.get("https://stepik.org/lesson/25969/step/8")