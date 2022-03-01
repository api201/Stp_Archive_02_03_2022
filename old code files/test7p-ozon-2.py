from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep, time

browser = webdriver.Chrome()
#url = 'https://google.com'
#url = 'https://www.ozon.ru/highlight/new-year-343612/'
#url = 'https://www.eapteka.ru/'
url = 'https://www.labirint.ru/'

try:
    # open google.com
    browser.get(url)
    browser.maximize_window()
    #search = browser.find_element_by_tag_name('input')
    # search request for OZON.ru
    #search.send_keys('ozon.ru')
    #search.send_keys(Keys.RETURN)

    # locate by partial link and open ozon.ru
    #browser.find_element_by_partial_link_text('OZON — интернет-магазин').click()
    # sleep(5)
   # wait = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located(By.CSS_SELECTOR, "div[type='addToCartButton']"))

 #   tovar1 = browser.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[3]/div/div/div/button/span/span")
    #time.sleep(1)
 #   tovar1.click()

  #  prod_1 = browser.find_element_by_css_selector(
    #    "div.a1p4.a3j0.a1p6.co7.cp1:nth-child(3) div[type='addToCartButton']").click()

    #sleep(2)

    tovar1 = browser.find_element(By.XPATH, "//*[contains(text(), 'КОРЗИНУ')]")
    tovar1.click()

    sleep(2)

    tovar2 = browser.find_element(By.XPATH, "//*[contains(text(), 'КОРЗИНУ')]")
    tovar2.click()

    sleep(3)

  #  tovar3 = browser.find_element(By.XPATH, "//*[contains(text(), 'КОРЗИНУ')]")
  #  tovar3.click()

    sleep(3)

    oformit = browser.find_element(By.XPATH, "//*[contains(text(), 'Оформить')]")
    oformit.click()

    sleep(3)

    #itogo = browser.find_element(By.XPATH, "//*[@id='ui-id-4']/b")
    itogo = browser.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[3]/div/div/div/div/div/div[2]/div/div[3]/div/div/div/div/ul/li[1]/a/b")

    print(itogo)
    print('\n')

 #   prod_1 = browser.find_element_by_css_selector(".ui-e6").click()

 #   prod_2 = browser.find_element_by_css_selector(
     #   "div.a1p4.a3j0.a1p6.co7.cp1:nth-child(4) div[type='addToCartButton']").click()

 #   prod_3 = browser.find_element_by_css_selector(
     #   "div.a1p4.a3j0.a1p6.co7.cp1:nth-child(5) div[type='addToCartButton']").click()

  #  cart = browser.find_element_by_css_selector("a[href='/cart/']").click()
 #   wait1 = WebDriverWait(browser, 20).until(EC.element_to_be_selected(By.CSS_SELECTOR, '.container:nth-child(3) .a7m4'))
 #   goods = browser.find_elements_by_css_selector('.container:nth-child(3) .a7m4')

 #   print(goods)
 #   print(len(goods))

 #   assert len(goods) == 3, 'в корзине не 3 вещи'
finally:
    sleep(3)
   # browser.close()
    browser.quit()