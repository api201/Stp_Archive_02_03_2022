import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(link)

        first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("BILL")
        second_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("GATES")
        send_email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("BILL_GATES@WINDOWS.COM")
        phone = browser.find_element(By.XPATH, "//*[normalize-space(.)='Phone:']/input").send_keys("+7-495-444-55555")
        adress = browser.find_element(By.XPATH, "//label[text()=\'Address:\']/following-sibling::input").send_keys("LONDON")
        # time.sleep(2)
        submit_btn = browser.find_element(By.XPATH, "//*[text()='Submit']").click()

        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(link)

        first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("BILL")
        second_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("GATES")
        send_email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("BILL_GATES@WINDOWS.COM")
        phone = browser.find_element(By.XPATH, "//*[normalize-space(.)='Phone:']/input").send_keys("+7-495-444-55555")
        adress = browser.find_element(By.XPATH, "//label[text()=\'Address:\']/following-sibling::input").send_keys("LONDON")
        # time.sleep(2)
        submit_btn = browser.find_element(By.XPATH, "//*[text()='Submit']").click()

        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

if __name__ == "__main__":
    unittest.main()

#python -m unittest test-32-4.py