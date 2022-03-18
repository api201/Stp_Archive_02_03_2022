import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_quest_should_see_add_to_basket_button(browser):
 link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
 browser.get(link)
 text_btn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
 print("\n")
 print("Text of button is: ", text_btn.text, "\n")
 assert text_btn == browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
 time.sleep(3)