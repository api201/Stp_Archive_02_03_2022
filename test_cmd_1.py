from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\geckodriver05feb\geckodriver.exe', options=options)

driver.get("https://stepik.org/lesson/25969/step/8")