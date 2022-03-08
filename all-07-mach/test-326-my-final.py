import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

wtext = "Congratulations! You have successfully registered!"
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

def fill_form(link):
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)
    first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("BILL")
    second_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("GATES")
    send_email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("BILL_GATES@WINDOWS.COM")
    submit_btn = browser.find_element(By.XPATH, "//*[text()='Submit']").click()
    return browser.find_element(By.TAG_NAME, "h1").text

class TestReg(unittest.TestCase):
    def test_reg_posivite(self):
        self.assertEqual(fill_form(link1), wtext, "registration is failed")

    def test_reg_negative(self):
        self.assertEqual(fill_form(link2), wtext, "registration is failed")

if __name__ == "__main__":
    unittest.main()

#python -m test-326-my-final.py